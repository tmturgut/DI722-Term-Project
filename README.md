
<div align="center">

# MIDDLE EAST TECHNICAL UNIVERSITY
### DI722 - Spatio-Temporal Data Mining
#### Project Proposal Presentation

<br>

## Spatio-Temporal Analysis of Flood Risk and Social Vulnerability <br> using H3 Grids and DBSCAN in UK

<br>

**Turgut Muhammet TURGUT** <br>
Civil Engineering Department <br>
Water Resources Division <br>
2786416 <br>

<br>

<img width="137.25" height="75" alt="8 2" src="https://github.com/user-attachments/assets/8f8140b7-7c22-4f92-b7f3-fd7cf785c1d8" />

**08/05/2026**

</div>

<hr>

  
  
<h1 align="center">Introduction</h1>
 &nbsp;&nbsp;&nbsp;&nbsp; In the UK, extreme weather events—especially flooding—have become much more frequent and severe due to climate change. However, the effects of these environmental risks are intricately linked to social injustices rather than being solely a physical or infrastructure issue. Communities that are socially vulnerable and impoverished frequently live in high-risk flood zones and typically lack the social and economic resources needed for quick recovery and resilience. This term project's main goal is to identify and examine the spatial connections between social deprivation and flood hazards. This study attempts to map these overlapping risks using open-source data from the UK Environment Agency (flood risk areas) and the UK Government's Index of Multiple Deprivation (IMD).
 
## Study Area
 &nbsp;&nbsp;&nbsp;&nbsp; This term project's geographical focus includes the Thames River Basin in the United Kingdom and the Greater London area. Because of its unique combination of complex riverine and coastal flood exposure along with a variety of socioeconomic neighborhood profiles, this area was chosen as the spatial bounding box (Extent: X: 499000 to 585000, Y: 138000 to 191000 in EPSG:27700, British National Grid). 
 
## Dataset Introduction
 To achieve the objectives of this spatial data mining project, two distinct and open-source datasets from the United Kingdom are utilized. These datasets provide the foundational physical and socio-economic variables required for the clustering analysis.

 ###  Data Availability
Due to GitHub's file size limitations, the generated spatial databases (.gpkg) containing the H3 DGGS polygons and K-Means baseline results are hosted externally. You can access and download the raw project data via the link below:
* Download Spatial Datasets (Google Drive) https://drive.google.com/drive/folders/1IG0fhf6xswQtRZa08rku30DNGrf6z_oa?usp=drive_link


### 1. Flood Hazard Data (Physical Dimension)
Source: UK Environment Agency (EA) Open Data portal.

Dataset: Risk of Flooding from Rivers and Sea (RoFRS) or historical Flood Warnings.

Format: Spatial vector data (Shapefile / GeoPackage).

Description: This spatial dataset maps the geographical extent and probability of flood risks across the selected study area. It serves as the primary environmental hazard indicator, delineating which regions are geographically exposed to potential inundation.

### 2. Social Vulnerability Data (Socio-economic Dimension)
Source: UK Government Open Data.

Dataset: The English Indices of Deprivation / Index of Multiple Deprivation (IMD).

Format: Tabular data (CSV) coupled with spatial boundaries.

Description: The IMD evaluates relative deprivation across neighborhoods by combining various domains such as income, employment, education, and health into a single score. In this project, it represents the social vulnerability and resilience capacity of the populations residing within the study area.

### Data Integration Strategy
 &nbsp;&nbsp;&nbsp;&nbsp; The Uber H3 Discrete Global Grid System (DGGS) will be used to harmonize these datasets because they have essentially different formats (tabular data for social indices and spatial polygons for floods). The IMD deprivation scores and the flood risk percentages will be combined into homogeneous H3 hexagonal cells (e.g., Resolution 8) to produce a standardized, clean dataset that is prepared for machine learning algorithms.

## General Description of the Baseline Method
&nbsp;&nbsp;&nbsp;&nbsp;  In this term project, K-Means Clustering is selected as the baseline machine learning method. K-Means is a highly efficient, unsupervised learning algorithm that partitions data into distinct clusters based on feature similarity. The integrated dataset, structured within the H3 hexagonal grid system, contains both physical flood hazard probabilities and socio-economic deprivation (IMD) scores. This data will be fed into the K-Means algorithm to group the spatial units (hexagons) into fundamental categories, such as Low, Moderate, and High-Risk clusters.

 &nbsp;&nbsp;&nbsp;&nbsp; At this baseline stage, the clustering relies on the statistical attributes of the data rather than their geographical proximity or spatial density. The reason for establishing this K-Means as a baseline is:
•	It provides a fundamental understanding of the statistical correlations between flood exposure and social vulnerability.
•	it serves as a performance benchmark.

 &nbsp;&nbsp;&nbsp;&nbsp; In the subsequent phases of the project, this attribute-based baseline will be compared against advanced spatial algorithms, specifically DBSCAN (Density-Based Spatial Clustering of Applications with Noise). This comparison will demonstrate the added value of incorporating spatial neighborhood dynamics and density into identifying critical vulnerability hotspots.

<h1 align="center">Literature Review</h1>

## 1.	'Bunkering down': How one community is tightening social-ecological network structures in the face of global change.
**DOI:** [10.1002/pan3.10364](https://doi.org/10.1002/pan3.10364)

### Relevance to the Term Project
 &nbsp;&nbsp;&nbsp;&nbsp; This article provides the sociological foundation for the term project. It proves that vulnerable communities facing environmental risks naturally form isolated clusters ("bunkering down"), justifying the use of spatial clustering algorithms (K-Means and DBSCAN) to identify vulnerability hotspots.
#### Subject
&nbsp;&nbsp;&nbsp;&nbsp;The temporal evolution of social-ecological networks in a vulnerable community facing escalating environmental changes.
### Inputs
&nbsp;&nbsp;&nbsp;&nbsp;Household communication surveys, trophic fish interactions, and socio-demographic attributes (e.g., clan, wealth).
### Method
&nbsp;&nbsp;&nbsp;&nbsp;Dynamic network modeling using temporal and cross-sectional exponential random graph models (TERGM & ERGM).
### Outputs
&nbsp;&nbsp;&nbsp;&nbsp;  Faced with risks, the community "bunkers down," forming tight-knit, isolated social clusters (homophily) and relying on traditional leaders rather than seeking diverse external support.
### Data Sources & Resolutions
 &nbsp;&nbsp;&nbsp;&nbsp; The study draws on primary quantitative and qualitative data collected over a 16-year period (2002, 2009, 2012, 2016, and 2018). Contextual baseline data includes benthic community surveys (to track coral vs. macroalgae cover) and systematically sampled household surveys tracking population and expenditures. The specific network data was collected via structured in-person interviews (surveys) in 2016 and 2018. The resolution of the data is at the household level for the social network, the species level for the ecological network, and the individual gear-to-species level for social-ecological links
### Models / Software Used
&nbsp;&nbsp;&nbsp;&nbsp;  The researchers used the MPNet software to implement the TERGM and ERGM procedures, obtain parameter estimates, and evaluate the Goodness of Fit for the modeled networks.

## 2.	Discrete Global Grid Systems as scalable geospatial frameworks for characterizing coastal environments
**DOI:** [10.1016/j.envsoft.2021.105210](https://doi.org/10.1016/j.envsoft.2021.105210)

### Relevance to the Term Project
 &nbsp;&nbsp;&nbsp;&nbsp; Fulfills the project requirement to investigate DGGS/H3. It justifies our use of H3 to seamlessly harmonize disparate datasets (flood polygons and tabular socio-economic data) and proves H3's high performance in spatial neighborhood identification, which is mathematically essential for our distance and density-based algorithms (K-Means and DBSCAN).
### Subject
  &nbsp;&nbsp;&nbsp;&nbsp;Exploring hexagon-based DGGS (specifically H3 and dggridR) as scalable frameworks to aggregate and integrate diverse coastal data across the land-sea interface.
### Inputs
 &nbsp;&nbsp;&nbsp;&nbsp; Point (water temperatures), line (shorelines), and grid (sea surface temperatures) datasets from Tampa Bay, FL, alongside existing spatial boundaries (e.g., NHDPlus, HUC-08).
### Method
&nbsp;&nbsp;&nbsp;&nbsp;  Comparing H3 and dggridR by matching hexagon areas to existing spatial frameworks, aggregating multi-format datasets into hex units, and testing networking and interpolation capabilities.
### Outputs
  &nbsp;&nbsp;&nbsp;&nbsp;Both systems are effective. While dggridR offers flexible scaling, H3 is significantly more performant and computationally efficient for spatial indexing, identifying neighbors, and scaling data without relying on external flow tables.
### Data Sources & Resolutions
 &nbsp;&nbsp;&nbsp;&nbsp; The study focused on the Tampa Bay estuary. Water Quality Portal point data consisted of water temperature results collected between 1995 and 2020. Gridded data was derived from 1-km resolution daily sea surface temperature satellite datasets. Existing spatial framework benchmarks varied in resolution: local NHDPlus catchments (~2.0-2.9 km²), sub-estuary ATTAINS waterbodies (~22 km²), estuary WBD HUC-08 units (~1800 km²), and 30x30-meter elevation grid cells.
### Models / Software Used
&nbsp;&nbsp;&nbsp;&nbsp;  The researchers used the H3 python library (v3.6.4) and the dggridR R package (v2.0.4), which implements the DGGRID software (v6.2b). Data gathering, pre-processing, and demonstration analyses were run using automated Python scripts within Jupyter Notebooks.

## 3.	Flood susceptibility modelling using advanced ensemble machine learning models
**DOI:** [10.1016/j.gsf.2020.09.006](https://doi.org/10.1016/j.gsf.2020.09.006)

### Relevance to the Term Project
&nbsp;&nbsp;&nbsp;&nbsp;  Provides crucial empirical justification for our algorithmic progression. It proves that analyzing complex spatial flood hazards requires advanced machine learning techniques, perfectly justifying our transition from a simple baseline model (K-Means) to a sophisticated, density-based advanced algorithm (DBSCAN).
### Subject
  &nbsp;&nbsp;&nbsp;&nbsp;Evaluating advanced hybrid ensemble ML models (e.g., Dagging, Random Subspace) for high-performance flood susceptibility mapping in the Teesta River basin, Bangladesh.
### Inputs
 &nbsp;&nbsp;&nbsp;&nbsp; The study utilized twelve flood influencing factors: elevation, curvature, aspect, slope, topographic roughness index (TRI), topographic wetness index (TWI), stream power index (SPI), sediment transport index (STI), land use/land cover (LULC), distance to river, soil type, and rainfall. Also, 413 historical/current flooding points.
### Method
  &nbsp;&nbsp;&nbsp;&nbsp;Assessing factor relationships via InGR and multicollinearity tests, followed by modeling flood susceptibility using 5 ML approaches (ANN, SVM, RF, RS, and Dagging). Models were validated using ROC/AUC, RMSE, and non-parametric statistical tests.
### Outputs
  &nbsp;&nbsp;&nbsp;&nbsp;The proposed Dagging ensemble model significantly outperformed others (AUC 0.873). LULC, distance to river, elevation, and slope were the most significant drivers, classifying 29.62% of the total area as extremely vulnerable.
### Data Sources & Resolutions
 &nbsp;&nbsp;&nbsp;&nbsp; All spatial influencing factors were transformed into raster format with a 30m spatial resolution. Topographical variables were derived from ASTER GDEM (Version 2, 30m resolution). LULC maps were created using Landsat and Operational Land Imager (OLI) imagery (30m resolution). Soil data was sourced from the USDA NRCS soil taxonomy map. Rainfall data came from the Bangladesh Meteorological Department and was interpolated using Kriging. Drainage networks and distance to rivers were derived from topographic maps at a 1:250,000 scale provided by the Bangladesh Water Development Board and Google Earth.
### Models / Software Used
 &nbsp;&nbsp;&nbsp;&nbsp; WEKA package (version 3.9.3): Used to execute the machine learning models (ANN, SVM, RF, RS, and Dagging). ArcGIS 10.2 / 10.5: Utilized for handling spatial datasets, deriving topographical factors, and final mapping. ENVI software (version 5.3): Used to classify the LULC map with an artificial neural network.

<h1 align="center">DGGS (H3) Investigation</h1>

  &nbsp;&nbsp;&nbsp;&nbsp;The Uber H3 Discrete Global Grid System (DGGS) is used as the fundamental spatial framework for this study in compliance with the project guidelines. 
  
 &nbsp;&nbsp;&nbsp;&nbsp;The flood hazard data consists of complex spatial polygons (representing physical inundation boundaries), while the Index of Multiple Deprivation (IMD) is primarily tabular socio-economic data linked to census tracts. By implementing H3 hexagonal grids (e.g., at Resolution 8), these fundamentally disparate geospatial data types are harmonized into uniform spatial units. Each hexagon acts as a unified data bin that calculates and stores both the percentage of flood risk coverage and the relative social deprivation score within its boundaries.
  
  &nbsp;&nbsp;&nbsp;&nbsp;Furthermore, the geometric properties of H3 hexagons provide a significant analytical advantage over traditional square grids. Hexagons possess equidistant centroids and uniform neighboring distances. This characteristic is important for the spatial data mining phase of this project, as it significantly enhances the accuracy, neighbor-identification performance, and reliability of distance-based and density-based clustering algorithms, specifically K-Means and DBSCAN.

<h1 align="center">Preliminary Results</h1>

### H3 Discrete Global Grid System (DGGS) Part

&nbsp;&nbsp;&nbsp;&nbsp;The initial phase of the project involved importing and preprocessing the spatial datasets within a Python environment using Google Colab. The UK LSOA boundary data was processed utilizing the geopandas and h3 libraries to generate the foundational Discrete Global Grid System (DGGS) at Resolution 8. During the H3 hex-binning process, several invalid geometries and topological errors were detected within the clipped boundary data. Instead of algorithmic failure, a try-except validation pipeline was implemented to isolate and skip these corrupted multi-polygons, ensuring a robust and clean H3 spatial grid for further analysis.

&nbsp;&nbsp;&nbsp;&nbsp;Following the generation of the grid, the H3 hexagons were exported and visualized in QGIS. The preliminary maps below (FIG.1) demonstrate the overlay of the transparent H3 grid with the physical flood hazard polygons (RoFRS). The baseline (K-Means) clustering phase is made possible by this visual output, which validates the spatial data integration for the term project.

<div align="center">

<img width="1430" height="623" alt="Fig1_Preliminary Result" src="https://github.com/user-attachments/assets/dfe132e6-9f23-47ad-8439-6167068e5e49" />

<br>

<i><b>Fig. 1:</b> Spatial integration of complex flood extent polygons within the scalable H3 Discrete Global Grid System (DGGS) framework.</i>

</div>


### Baseline Method Part
&nbsp;&nbsp;&nbsp;&nbsp; In accordance with the project guidelines, **K-Means Clustering** was selected as the baseline method to serve as a fundamental reference point for evaluating more advanced spatial data mining algorithms. To construct this model, the study area was tessellated into the H3 Discrete Global Grid System (DGGS) at Resolution 8. 

Two critical features were engineered for each hexagonal cell using spatial join and overlay techniques:
1. **Flood Percentage:** The area ratio of the UK Environment Agency's flood risk polygons (`rofrs_4band`) intersecting with the cell.
2. **Social Deprivation Score:** The Index of Multiple Deprivation (IMD) score extracted from the underlying LSOA boundaries.

The K-Means algorithm (`k=3`) was then applied to these two features, mathematically categorizing the geographic space into three distinct risk clusters: **Medium Risk (0), High Risk (1), and Low Risk (2)**, without providing any prior geographic coordinate information to the machine.

---

 The baseline clustering results were visualized in QGIS by categorizing the H3 grids based on their assigned `Risk_Cluster` values.

<div align="center">

<img width="966" height="429" alt="Fig2_BaselineMethodResult" src="https://github.com/user-attachments/assets/c09dbc3b-f986-4cc8-b34a-5807a04b185a" />
<br>

<i><b>Fig. 2:</b> Spatial distribution of K-Means baseline clustering (Green: Low Risk [Cluster 2], Yellow: Medium Risk [Cluster 0], Red: High Risk [Cluster 1]) overlaid with actual flood extent polygons (blue) within the scalable H3 DGGS framework.</i>

</div>

<h1 align="center">Analysis of the Baseline Output</h1>

&nbsp;&nbsp;&nbsp;&nbsp;The generated heatmap demonstrates a consistent spatio-temporal pattern. As visually verified in **Fig. 2**, the 'High Risk' clusters (**Cluster 1**, represented by red hexagons) strongly coincide with the physical distribution of river and sea flooding areas (blue polygons). Furthermore, the transition zones (**Cluster 0**, represented by yellow hexagons) buffer these critical areas. This initial outcome demonstrates that the baseline machine learning model effectively captures the intricate relationship between socioeconomic deprivation and physical flood hazards.

### Statistical Evaluation of the Baseline Model
In addition to the spatial distribution, a detailed statistical evaluation was conducted to understand the mathematical behavior of the K-Means algorithm and the characteristics of the identified clusters.

<div align="center">
  
<img width="794" height="93" alt="Figure_1" src="https://github.com/user-attachments/assets/39ea08c0-2449-4ee0-8a65-2b590eac4c83" />

<br>

<i><b>Fig. 3:</b> Summary Statistics of K-Means Risk Clusters.</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;This table presents the descriptive statistics of the three risk clusters generated by the baseline K-Means algorithm. It highlights that out of 222,330 H3 hexagons, 28,378 fall into the High-Risk category (Cluster 1). This specific cluster simultaneously exhibits the highest average flood risk (97%) and the most severe social deprivation score (31.01).

<div align="center">
  
<img width="2924" height="2245" alt="Figure_2" src="https://github.com/user-attachments/assets/8e9b71fc-8770-4102-a729-fe29f820f771" />

<br>

<i><b>Fig. 4:</b>Proportional Distribution of Regional Risk Clusters (K-Means).</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;The pie chart illustrates the areal distribution of the identified risk zones across the study area. Notably, 13% of the region is classified under the most critical threat level (Cluster 1), indicating the proportion of the area where severe physical flood hazards intersect with acute socioeconomic vulnerability.

<div align="center">

<img width="2772" height="2241" alt="Figure_3" src="https://github.com/user-attachments/assets/0c171916-1f76-4b82-93db-beae342a0c35" />

<br>

<i><b>Fig. 5:</b>Average Flood Risk and Social Deprivation Levels by Cluster.</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;The combo chart visually confirms the intersection of the two primary threat metrics. The blue columns represent the average flood risk (%), while the black trend line tracks the average Index of Multiple Deprivation (IMD) score. It clearly demonstrates that Cluster 1 (Red) peaks in both physical inundation probability and social disadvantage, mapping the areas with the lowest resilience capacity.

