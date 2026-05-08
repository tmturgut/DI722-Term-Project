import geopandas as gpd
import pandas as pd
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings('ignore')

print("1. Altlık Veriler Okunuyor...")
h3_grids = gpd.read_file("london_h3_grid_res8.gpkg")
lsoa_gdf = gpd.read_file("Lower_layer_Super_Output_Areas_Dec_2011_Boundaries_Full_Clipped_BFC_EW_V3_2022_-5365225720680633795.gpkg")
lsoa_gdf = lsoa_gdf.to_crs(epsg=4326)

print("2. Sosyal Kırılganlık CSV Verisi Okunuyor...")
csv_filename = "File_7_-_All_IoD2019_Scores__Ranks__Deciles_and_Population_Denominators_3.csv" 
imd_df = pd.read_csv(csv_filename)

lsoa_code_col = [col for col in lsoa_gdf.columns if 'lsoa' in col.lower() and 'cd' in col.lower()]
if not lsoa_code_col:
    lsoa_code_col = [col for col in lsoa_gdf.columns if 'code' in col.lower()]
target_lsoa_col = lsoa_code_col if isinstance(lsoa_code_col, list) and len(lsoa_code_col) > 0 else "lsoa11cd"

lsoa_merged = lsoa_gdf.merge(imd_df, left_on=target_lsoa_col, right_on='LSOA code (2011)', how='left')

print("3. Spatial Join İşlemi...")
h3_centroids = h3_grids.copy()
h3_centroids['geometry'] = h3_centroids.geometry.centroid
h3_social = gpd.sjoin(h3_centroids, lsoa_merged, how='left', predicate='intersects')
h3_social = h3_social.set_geometry(h3_grids.geometry)

print("4. Taşkın Yüzdesi Hesaplanıyor...")
flood_data = gpd.read_file("rofrs_4band.gdb")
flood_data = flood_data.to_crs(epsg=4326)

flood_intersection = gpd.overlay(h3_social, flood_data, how='intersection')
flood_intersection['flood_area'] = flood_intersection.geometry.area
h3_social['total_area'] = h3_social.geometry.area

flood_grouped = flood_intersection.groupby('h3_id')['flood_area'].sum().reset_index()
final_data = h3_social.merge(flood_grouped, on='h3_id', how='left')
final_data['flood_area'] = final_data['flood_area'].fillna(0)
final_data['flood_percentage'] = (final_data['flood_area'] / final_data['total_area']) * 100

print("5. BASELINE MODEL (K-MEANS) ÇALIŞTIRILIYOR...")
score_column = 'Index of Multiple Deprivation (IMD) Score' 
ml_features = final_data[[score_column, 'flood_percentage']].fillna(0)

kmeans = KMeans(n_clusters=3, random_state=42)
final_data['Risk_Cluster'] = kmeans.fit_predict(ml_features)

print("6. Sonuçlar Kaydediliyor...")
output_filename = "london_h3_kmeans_baseline.gpkg"
final_data.to_file(output_filename, driver="GPKG")
print(f"BAŞARILI! Sonuç: '{output_filename}'")