import geopandas as gpd
import pandas as pd

print("1. Loading the DBSCAN output file...")
# Read the advanced method spatial results
input_file = "london_h3_dbscan_advanced.gpkg"
gdf = gpd.read_file(input_file)

print("2. Calculating summary statistics for each cluster...")
# Calculate cell count, average flood risk, and average IMD score for all clusters (including noise: -1)
cluster_summaries = gdf.groupby('DBSCAN_Cluster').agg(
    Number_of_Hexagons=('DBSCAN_Cluster', 'count'),
    Average_Flood_Risk=('flood_percentage', 'mean'),
    Average_IMD_Score=('Index of Multiple Deprivation (IMD) Score', 'mean')
).reset_index()

print("3. Categorizing clusters for data visualization...")
# Label clusters to easily distinguish true hotspots, wealthy flooded areas, noise, and others
def categorize_cluster(row):
    if row['DBSCAN_Cluster'] in [1, 2]:
        return 'True Hotspots (Red Alert - Cluster 30 & 33)'
    elif row['DBSCAN_Cluster'] == 11:
        return 'Flooded but Wealthy (Low Vulnerability - Cluster 11)'
    elif row['DBSCAN_Cluster'] == -1:
        return 'Spatial Noise (Isolated Cells)'
    else:
        return 'Low/Medium Risk or Single Hazard'

# Apply the labels to a new column
cluster_summaries['Category'] = cluster_summaries.apply(categorize_cluster, axis=1)

print("4. Exporting data to CSV...")
# Save the summary table as a CSV file to create charts in Excel
csv_filename = "dbscan_statistics_for_excel.csv"
cluster_summaries.to_csv(csv_filename, index=False)
print(f"SUCCESS! File saved as: '{csv_filename}'")