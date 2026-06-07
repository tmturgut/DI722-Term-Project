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

print("3. Categorizing clusters dynamically for data visualization...")
# Dynamically label clusters based on their actual statistical values instead of hardcoded IDs
def categorize_cluster(row):
    # DBSCAN her zaman gürültüyü -1 olarak atar, bu sabittir ve güvenlidir.
    if row['DBSCAN_Cluster'] == -1:
        return 'Spatial Noise (Isolated Cells)'
    
    # Gerçek Hotspot: Hem taşkın riski yüksek (örn. >%20) hem de IMD skoru çok yüksek (örn. >20)
    elif row['Average_Flood_Risk'] > 20 and row['Average_IMD_Score'] > 20:
        return 'True Hotspots (Red Alert)'
        
    # Seli yiyen ama zengin: Taşkın riski çok yüksek (örn. >%50) ama IMD skoru düşük (örn. <15)
    elif row['Average_Flood_Risk'] > 50 and row['Average_IMD_Score'] < 15:
        return 'Flooded but Wealthy (Low Vulnerability)'
        
    # Geri kalan normal kümeler
    else:
        return 'Low/Medium Risk or Single Hazard'

# Apply the dynamic labels to a new column
cluster_summaries['Category'] = cluster_summaries.apply(categorize_cluster, axis=1)

print("4. Exporting data to CSV...")
# Save the summary table as a CSV file to create charts in Excel
csv_filename = "dbscan_statistics_for_excel.csv"
cluster_summaries.to_csv(csv_filename, index=False)
print(f"SUCCESS! File saved as: '{csv_filename}'")
