import geopandas as gpd
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import warnings
warnings.filterwarnings('ignore')

print("1. Loading baseline dataset...")
# Read the baseline output containing Flood Risk and IMD Score data
input_file = "london_h3_kmeans_baseline.gpkg"
gdf = gpd.read_file(input_file)

print("2. STEP 1: Centroid extraction...")
# Extract X and Y coordinates from hexagon geometries for spatial analysis
gdf['Longitude'] = gdf.geometry.centroid.x
gdf['Latitude'] = gdf.geometry.centroid.y

print("3. STEP 2: Feature scaling...")
# Standardize the features to ensure equal weight during clustering
score_column = 'Index of Multiple Deprivation (IMD) Score'
ml_features = gdf[[score_column, 'flood_percentage', 'Longitude', 'Latitude']].fillna(0)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(ml_features)

print("4. STEP 3 & 4: Setting DBSCAN parameters and filtering noise...")
# Define DBSCAN parameters
epsilon_val = 0.3  # Maximum distance between two samples to be considered as neighbors
min_pts = 5        # Minimum number of samples in a neighborhood to form a core point (hotspot)

# Initialize and fit the DBSCAN model
dbscan = DBSCAN(eps=epsilon_val, min_samples=min_pts)
gdf['DBSCAN_Cluster'] = dbscan.fit_predict(scaled_features)

print("5. Saving the new spatial dataset...")
# Export the results to a new GeoPackage file for visualization
output_filename = "london_h3_dbscan_advanced.gpkg"
gdf.to_file(output_filename, driver="GPKG")

# Print summary statistics
noise_count = (gdf['DBSCAN_Cluster'] == -1).sum()
hotspot_count = (gdf['DBSCAN_Cluster'] != -1).sum()

print("--- ANALYSIS SUMMARY ---")
print(f"Number of Noise/Outlier cells (-1): {noise_count}")
print(f"Number of Hotspot/Clustered cells: {hotspot_count}")
print(f"SUCCESS! Output saved as: '{output_filename}'")