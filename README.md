
<div align="center">

# MIDDLE EAST TECHNICAL UNIVERSITY
### DI722 - Spatio Temporal Data Mining
#### Final Project Presentation

<br>

## Spatio Temporal Analysis of Flood Risk and Social Vulnerability in the UK <br> Comparing K-Means and DBSCAN on H3 Grids

<br>

**Turgut Muhammet TURGUT** <br>
Civil Engineering Department <br>
Water Resources Division <br>
2786416 <br>

<br>

<img width="137.25" height="75" alt="8 2" src="https://github.com/user-attachments/assets/8f8140b7-7c22-4f92-b7f3-fd7cf785c1d8" />

**12/06/2026**

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

 &nbsp;&nbsp;&nbsp;&nbsp;  *"To establish a purely attribute-based baseline, the K-Means algorithm was intentionally trained without geographic coordinates (spatially blind). This highlights the limitations of traditional models, which is subsequently addressed by DBSCAN's spatial density awareness utilizing Latitude and Longitude."

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
&nbsp;&nbsp;&nbsp;&nbsp;Algorithmic Translation of the Theory

&nbsp;&nbsp;&nbsp;&nbsp;Rather than focusing on the statistical network software (TERGM/ERGM) used in the original study, our term project translates the sociological concept of "bunkering down" into a spatial data mining framework. We operationalize this theory by utilizing spatial clustering algorithms (**K-Means and DBSCAN** via Python's `scikit-learn`). These algorithms allow us to geographically pinpoint the isolated, socially vulnerable communities that lack bridging social capital during environmental disasters, successfully identifying and mapping them as severe socio-environmental "Hotspots" (Red Alert zones) across the UK.

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


### Baseline Method (K-MEAN) Results
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

<h1 align="center">Technical Note</h1>

### Spatial Gaps and H3 Tessellation Dynamics

&nbsp;&nbsp;&nbsp;&nbsp;Visual inspections of the generated H3 grid (as seen in the mapping outputs) reveal several un-tessellated gaps (white spaces) within the UK terrestrial boundaries. These gaps are not processing errors; rather, they are the mathematically correct outcomes of integrating real-world census geometries with rigid Discrete Global Grid Systems (DGGS). 

&nbsp;&nbsp;&nbsp;&nbsp;A custom `try-except` validation pipeline combined with a `.buffer(0)` geometric correction was implemented in the Python generation script to handle these edge cases without terminating the global loop. The absence of hexagonal cells in specific regions can be attributed to three primary spatio-topological factors:

| Phenomenon | Description | Impact on H3 Generation |
| :--- | :--- | :--- |
| **Demographic Voids (LSOA Nature)** | LSOA boundaries are delineated strictly by population density. Large unpopulated physical features (e.g., the River Thames channel, broad lakes, national parks) lack demographic data and thus correspond to empty spaces in the raw spatial input. | No underlying polygon exists to be tessellated, resulting in valid geographical gaps in the grid. |
| **Topological Slivers & Invalid Geometries** | The highly complex coastal and riverine boundaries of the UK contain microscopic self-intersections or sliver polygons. While `.buffer(0)` resolved most anomalies, extreme topological distortions violate the strict geometrical rules of the H3 `polyfill` algorithm. | The algorithm safely identifies these as mathematically invalid and skips them (handled via the `except: pass` block) to prevent system crashes. |
| **Resolution Limits (Centroid Exclusion)** | At H3 Resolution 8, each hexagon covers approximately 0.73 km². If a multi-polygon feature (such as a narrow coastal strip or a thin infrastructure corridor) is too narrow to encompass the mathematical centroid of an H3 cell, it cannot be tessellated. | Narrow/micro-polygons are filtered out automatically, ensuring that only statistically robust areas are processed for machine learning. |

&nbsp;&nbsp;&nbsp;&nbsp;This rigorous filtering mechanism ensures that the downstream machine learning algorithms (K-Means and DBSCAN) are fed exclusively with mathematically sound and demographically valid spatial data, enhancing the overall reliability of the Spatio-Temporal Data Mining process.

</div>

<h1 align="center">Analysis of the Baseline Method (K-MEAN) Results</h1>


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

&nbsp;&nbsp;&nbsp;&nbsp;The combo chart visually confirms the intersection of the two primary threat metrics. The yellow/green/red columns represent the average flood risk (%), while the black trend line tracks the average Index of Multiple Deprivation (IMD) score. It clearly demonstrates that Cluster 1 (Red) peaks in both physical inundation probability and social disadvantage, mapping the areas with the lowest resilience capacity.

<div align="center">

<img width="2662" height="2222" alt="Figure_4" src="https://github.com/user-attachments/assets/bccf9fee-aeba-4f5c-9883-b9a255b3cf16" />

<br>

<i><b>Fig. 6:</b>K-Means Cluster Distribution: Flooding vs. Social Deprivation.</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;This scatter plot, obtained with our baseline model K-Means, clearly demonstrates the algorithm's vulnerability to feature scaling issues. It forms rigid, horizontal boundaries primarily driven by the Social Deprivation (IMD Score) axis, failing to meaningfully integrate the spatial realities of Flood Risk. For instance, cells with near 100% flood risk are misclassified into lower risk clusters simply because their IMD scores fall below the algorithm's mathematical threshold. Furthermore, K-Means forces every data point into a cluster without identifying spatial noise. This statistically rigid and spatially blind nature of K-Means scientifically justifies our transition to a density-based 'Advanced Method' like DBSCAN to capture true, multidimensional geographic hotspots.

</div>

<h1 align="center">Additional Literature Review</h1>

## 4. Urban flood risk assessment based on DBSCAN and K-means clustering algorithm
**DOI:** [10.1080/19475705.2023.2250527](https://doi.org/10.1080/19475705.2023.2250527)

### Relevance to the Term Project
&nbsp;&nbsp;&nbsp;&nbsp; This article directly supports the methodological core of the term project. By systematically integrating DBSCAN and K-Means algorithms for urban flood risk assessment, it provides robust academic validation for our decision to use K-Means as an exploratory baseline and DBSCAN as an advanced method to filter spatial noise and precisely identify socio-environmental vulnerability hotspots.
#### Subject
&nbsp;&nbsp;&nbsp;&nbsp; Developing an efficient urban flood risk assessment framework by combining subjective-objective weighting methods with density-based (DBSCAN) and partition-based (K-means) spatial clustering algorithms to classify risk levels in urban areas.
### Inputs
&nbsp;&nbsp;&nbsp;&nbsp; A comprehensive set of 11 hazard and vulnerability indices: average annual precipitation (AP), heavy precipitation days (R50, R20), digital elevation model (DEM), slope (SL), river network density (RND), runoff coefficient (RC), population density (PD), GDP per unit area (GPUA), GDP per capita (GPC), and road network density (RD).
### Method
&nbsp;&nbsp;&nbsp;&nbsp;  The study uses a combinatorial empowerment approach (AHP and entropy weight method) to determine index weights [cite: 814, 816, 818]. DBSCAN is then applied to extract potential high-risk outliers (spatial noise), followed by the improved K-means++ clustering algorithm (optimized using the elbow method) to classify the remaining spatial data into distinct flood risk levels.
### Outputs
&nbsp;&nbsp;&nbsp;&nbsp; The hybrid clustering approach successfully classified the study area into five flood risk levels [cite: 831]. High-risk areas (3.79% of the total area) were found to be strongly associated with intense extreme rainfall, low elevation, gentle slopes, high runoff coefficients, and high population density [cite: 834, 835]. The integration of DBSCAN and K-Means proved superior to traditional TOPSIS methods and single K-Means by accurately pinpointing concentrated high-risk areas without underestimating localized hazardsm.
### Data Sources & Resolutions
&nbsp;&nbsp;&nbsp;&nbsp; lThe study focused on the municipal district of Fuzhou City, China [cite: 804]. Precipitation data (2011-2020) was sourced from the local Meteorological Service Center [cite: 806]. Land cover data was obtained from GlobeLand30 (30m resolution), population density from WorldPop (2020), economic data from the Fuzhou Statistical Yearbook, and road networks from OpenStreetMap. The spatial resolution for the risk assessment was standardized to a 100m x 100m grid, dividing the study area into 167,015 grid units.
### Models / Software Used
&nbsp;&nbsp;&nbsp;&nbsp; The researchers implemented the DBSCAN and K-means++ clustering algorithms. The Analytic Hierarchy Process (AHP) and Entropy weight models were used for statistical calculations.  ArcGIS was utilized for spatial analysis, grid division, and the visualization of the final flood risk maps.

## 5.	Profiles of social vulnerability for flood risk reduction
**DOI:** [[10.1016/j.ijdrr.2025.105250](https://doi.org/10.1016/j.ijdrr.2025.105250)
### Relevance to the Term Project
 &nbsp;&nbsp;&nbsp;&nbsp; This article provides strong conceptual and methodological justification for shifting from traditional aggregate vulnerability indices to spatial clustering approaches (profiles) [cite: 9, 10]. It scientifically validates our decision to use advanced spatial clustering (DBSCAN and K-Means) to model intersectional socio-environmental vulnerabilities, proving that clustering algorithms can pinpoint specific flood risk hotspots and tailored archetypes (e.g., "Flooded but Wealthy" vs. "True Hotspots") without losing critical demographic nuances.

#### Subject
&nbsp;&nbsp;&nbsp;&nbsp; Identifying major archetypes of compound social vulnerability in the context of flood exposure in the United States by generating spatial typologies (Social Vulnerability Profiles - SVPs) rather than relying on traditional aggregate vulnerability indices.

### Inputs
&nbsp;&nbsp;&nbsp;&nbsp; A robust set of 24 demographic census variables (e.g., age dependency, disability, linguistic isolation, rent, and unemployment), continental-scale fluvial and pluvial flood hazard data (500-year floodplain), and high-resolution building footprints to assess physical exposure.

### Method
&nbsp;&nbsp;&nbsp;&nbsp; The study utilized Principal Component Analysis (PCA) to reduce data collinearity, followed by Hierarchical Clustering on Principal Components (HCPC) using Ward’s method to group the data into distinct spatial profiles. The spatial autocorrelation of the resulting clusters was evaluated using join count statistics via a Monte-Carlo simulation.

### Outputs
&nbsp;&nbsp;&nbsp;&nbsp; Six distinct spatial profiles of social vulnerability and flood exposure emerged from the clustering analysis. The research revealed that places with similar aggregate vulnerability scores actually possess fundamentally different intersectional characteristics (e.g., high exposure combined with linguistic isolation vs. low exposure with age dependency). This proves that spatial clustering provides actionable, localized intelligence for equitable flood adaptation that traditional indices obscure.

### Data Sources & Resolutions
 &nbsp;&nbsp;&nbsp;&nbsp; The study focused on the Contiguous United States (CONUS) at the census tract scale, analyzing 82,737 tracts. Demographic data was sourced from the 2017–2021 American Community Survey (ACS) [cite: 18]. Flood grids (10m resolution) integrating fluvial and pluvial hazards were acquired from Fathom, and exposure was apportioned using 129 million Microsoft Building Footprints.

### Models / Software Used
&nbsp;&nbsp;&nbsp;&nbsp; The researchers implemented Hierarchical Clustering on Principal Components (HCPC) utilizing Ward's method to generate the multidimensional profiles, and employed join count statistics combined with permutation tests to measure spatial autocorrelation and spatial clustering effects.

</div>

<h1 align="center">Secondary Results</h1>

### Advanced Method (DBSCAN) Results

&nbsp;&nbsp;&nbsp;&nbsp;Building upon the preliminary baseline findings, Density-Based Spatial Clustering of Applications with Noise (DBSCAN) was implemented as the advanced method to overcome the spatial blindness and strict partitioning limitations of the K-Means algorithm.
To provide true spatial intelligence to the model, the dataset was enriched by extracting the geographic centroid coordinates (Longitude and Latitude) for each H3 hexagonal cell. A four-dimensional feature space was constructed comprising:
* Flood Percentage
* Social Deprivation (IMD) Score
* Longitude
* Latitude

&nbsp;&nbsp;&nbsp;&nbsp;To ensure equal mathematical weight during distance calculations and prevent features with larger numerical ranges from dominating the model, feature scaling (StandardScaler) was applied to the entire dataset.

&nbsp;&nbsp;&nbsp;&nbsp;The DBSCAN algorithm was then executed with optimized parameters (ϵ = 0.3, MinPts = 5). Unlike K-Means, which forces every cell into a predefined cluster, DBSCAN successfully identified isolated, non-cohesive cells as spatial noise (Label: -1) and filtered them out. The algorithm detected 48 distinct, geographically continuous clusters across the study area. Through subsequent statistical evaluation of these clusters, specific groupings (Clusters 30 and 33) were pinpointed as the true socio-environmental "Red Alert" hotspots, representing the exact intersection of severe physical flood risk and critical social vulnerability.

<div align="center">
  
<img width="1063" height="515" alt="Fig7" src="https://github.com/user-attachments/assets/b0f5b00d-513f-4ca1-91d6-58cb995ec010" />

<br>

<i><b>Fig. 7:</b>Spatial distribution of highly vulnerable socio-environmental hotspots identified by the advanced DBSCAN algorithm</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;As illustrated in Fig. 7, the DBSCAN algorithm successfully overcomes the spatial blindness of the baseline method. By evaluating geographical coordinates and spatial density, the algorithm filtered out isolated, non-cohesive cells as noise. Instead of broadly classifying thousands of cells as high-risk, it precisely isolated the true socio-environmental hotspots (Clusters 30 and 33), revealing the highly concentrated and geographically continuous areas of severe vulnerability.


<div align="center">

<img width="1063" height="515" alt="Fig8" src="https://github.com/user-attachments/assets/e01da4a2-ec46-4245-8a0e-b769ba5916af" />

<br>

<i><b>Fig. 8:</b>Spatial intersection of DBSCAN-detected vulnerability hotspots (red) with physical river and sea flood extent polygons (blue)</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;Fig. 8 demonstrates the real-world spatial validation of the advanced model. By overlaying the DBSCAN-detected hotspots (red) onto the UK Environment Agency's physical flood extent polygons (blue), a perfect spatial intersection is revealed. This proves that the algorithm accurately pinpointed the critical "Red Alert" zones where extreme physical inundation hazards directly coincide with areas of profound socio-economic deprivation, highlighting priority regions for emergency management and budget allocation.

<div align="center">

</div>

<h1 align="center">Analysis of the Advance Method (DBSCAN) Results</h1>

### Statistical and Spatial Evaluation of the Advanced Model
Building upon the initial exploratory findings, a comprehensive statistical and spatial evaluation was conducted to understand the advanced mathematical behavior of the DBSCAN algorithm. Unlike the baseline model, this evaluation highlights the algorithm's capability to incorporate spatial density, effectively filter out isolated spatial noise, and pinpoint genuine socio-environmental vulnerability hotspots. The characteristics and proportional distribution of these refined clusters are detailed below.

<div align="center">
  
<img width="1007" height="120" alt="Fig9" src="https://github.com/user-attachments/assets/3f040cb1-0c46-4221-8433-6b98a123374c" />

<br>

<i><b>Fig. 9:</b>Summary statistics of socio-environmental risk categories identified via DBSCAN spatial clustering.</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;As detailed in Fig. 9, the advanced DBSCAN algorithm categorizes the H3 hexagonal grids into highly specific socio-environmental profiles based on spatial density. Unlike the baseline K-Means method, which broadly and inaccurately classified 28,378 cells as high-risk, DBSCAN precisely isolates the "True Hotspots" (Red Alert zones) to a highly concentrated spatial footprint of only 12 critical hexagons. Furthermore, the algorithm successfully identifies and filters out 839 geographically isolated cells as "Spatial Noise" (Label: -1), preventing potential resource misallocation. This statistical summary highlights the algorithm's advanced capability to differentiate between mere physical hazards (e.g., "Flooded but Wealthy" areas) and genuine multidimensional socio-environmental vulnerability.

<div align="center">
  
<img width="3377" height="2172" alt="Fig10" src="https://github.com/user-attachments/assets/05697c19-2e22-48a8-b1f7-455a3ca4d28d" />

<br>

<i><b>Fig. 10:</b>Proportional distribution of spatio-temporal risk clusters and isolated noise identified by the DBSCAN algorithm..</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;As depicted in Fig. 10, the DBSCAN algorithm drastically refines the risk proportions compared to the baseline K-Means model. While K-Means inaccurately classified 13% of the study area as high risk, the density-based DBSCAN model reveals that genuine "True Hotspots" (Red Alert zones) constitute a marginal fraction (0.01%) of the total area. Furthermore, it successfully filters out 0.38% of the cells as "Spatial Noise". This precise proportional distribution demonstrates the algorithm's capability to prevent the overestimation of risk and ensures that critical mitigation resources can be targeted exclusively toward mathematically robust, continuous hazard zones.

<div align="center">
  
<img width="3428" height="2154" alt="Fig11" src="https://github.com/user-attachments/assets/79ebf092-1a54-4f2f-b018-1c533c3d135e" />

<br>

<i><b>Fig. 11:</b>Average flood risk and socio-economic deprivation (IMD) levels across DBSCAN spatial categories.</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;As illustrated in Fig. 11, the combo chart visualizes the multidimensional nature of the identified spatial clusters. The algorithm effectively isolates the "Flooded but Wealthy" cluster (Cluster 11), which exhibits extreme physical vulnerability with an average flood risk of nearly 100%, yet possesses distinctively low social vulnerability (IMD: 7.43). Conversely, the "True Hotspots" category captures the areas experiencing simultaneous socio-environmental threats, marked by a significant flood risk (41.82%) coupled with severe social deprivation (IMD Score: 27.91). This nuanced distinction, which was completely obfuscated in the baseline K-Means model, proves the advanced algorithm's capability to differentiate between mere physical inundation and genuine socio-environmental vulnerability.

<div align="center">
  
<img width="4675" height="2653" alt="Fig12" src="https://github.com/user-attachments/assets/18399ead-818f-4572-b8f8-09928fa2d9ad" />

<br>

<i><b>Fig. 12:</b>Scatter plot of DBSCAN spatial clusters illustrating the relationship between average flood risk and socio-economic deprivation (IMD).</i>

</div>

&nbsp;&nbsp;&nbsp;&nbsp;As presented in Fig. 12, the scatter plot visually confirms the exceptional precision of the density-based clustering algorithm. Unlike the baseline K-Means method (see Fig. 6), which generated broad, overlapping horizontal bands of risk without considering geographic reality, DBSCAN intelligently condenses the grid cells into mathematically robust spatial clusters. By plotting the localized averages, the algorithm distinctly isolates specific anomalies—such as the "Flooded but Wealthy" cluster (Cluster 11) located in the extreme bottom-right quadrant (representing extreme flood risk but very low social deprivation)—and successfully separates isolated "Spatial Noise". Furthermore, the "True Hotspots" (Red Alert zones) are explicitly identified as isolated spatial pockets rather than a widespread continuous phenomenon. This distribution explicitly demonstrates the advanced algorithm's ability to filter out noise and provide precise, targeted intelligence for disaster mitigation strategies.

<h1 align="center">Conclusion: Baseline (K-MEAN) vs. Advanced (DBSCAN) Performance Comparison</h1>

&nbsp;&nbsp;&nbsp;&nbsp; The transition from the baseline K-Means model to the advanced DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm demonstrated a significant improvement in capturing the true spatial dynamics of flood vulnerability in Greater London. Based on the outputs of the spatial data mining processes, the advanced method outperformed the baseline in three critical areas:
1. Spatial Awareness vs. Attribute-Only Clustering: The baseline K-Means algorithm clustered the H3 hexagons solely based on statistical attributes (IMD score and Flood Percentage). As a result, it forced geographically distant and unrelated cells into the same risk category, ignoring spatial proximity. In contrast, the advanced DBSCAN model incorporated spatial features (Longitude and Latitude extracted from H3 centroids) alongside the standardized socio-environmental attributes. This allowed DBSCAN to identify true geographic "Hotspots" based on density, rather than arbitrary statistical groupings.
2. Handling Spatial Noise and Outliers: K-Means inherently forces every single hexagon into a cluster, which artificially skews the boundaries of vulnerability zones by including isolated, anomalous cells. The DBSCAN algorithm successfully mitigated this by filtering out spatial noise (categorized as Cluster -1). By isolating these outliers, the advanced method provided a much cleaner, more reliable map of contiguous high-risk zones that actually require emergency management interventions.
3. Precision in Socio-Environmental Risk Categorization: The advanced analysis generated detailed cluster summaries that allowed for nuanced vulnerability categorizations. While K-Means broadly labeled areas as High/Medium/Low risk, DBSCAN pinpointed specific intersections of environmental and social data. As shown in the advanced modeling outputs, the algorithm successfully distinguished between "Flooded but Wealthy" cells (high flood risk but low social vulnerability) and "True Hotspots" (Red alert zones with both high flood risk and severe social deprivation).

&nbsp;&nbsp;&nbsp;&nbsp; Conclusion: Overall, DBSCAN outperformed the baseline K-Means method by providing a density-based, spatially-aware, and noise-filtered analysis. This advanced method effectively translates raw socio-environmental datasets into actionable, contiguous vulnerability hotspots, proving that advanced spatial data mining algorithms are essential for complex urban hazard mapping.

