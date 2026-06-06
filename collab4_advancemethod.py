import pandas as pd

# Step 1: Filter out noise (-1) to keep only the actual clusters
valid_clusters = gdf[gdf['DBSCAN_Cluster'] != -1]

# Step 2: Calculate the number of cells, average flood risk, and average IMD score for each cluster
cluster_summaries = valid_clusters.groupby('DBSCAN_Cluster').agg(
    Cell_Count=('DBSCAN_Cluster', 'count'),
    Average_Flood_Percentage=('flood_percentage', 'mean'),
    Average_IMD_Score=('Index of Multiple Deprivation (IMD) Score', 'mean')
).reset_index()

# Step 3: Sort the clusters in descending order based on average flood percentage and IMD score
top_risk_clusters = cluster_summaries.sort_values(
    by=['Average_Flood_Percentage', 'Average_IMD_Score'], 
    ascending=[False, False]
)

# Print the top 5 most vulnerable hotspot clusters
print("--- TOP 5 MOST VULNERABLE HOTSPOT CLUSTERS IN THE UK ---")
print(top_risk_clusters.head(5).to_string(index=False))