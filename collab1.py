import geopandas as gpd
import h3
from shapely.geometry import Polygon
from h3 import LatLngPoly

input_file = "/content/Lower_layer_Super_Output_Areas_Dec_2011_Boundaries_Full_Clipped_BFC_EW_V3_2022_-5365225720680633795.gpkg"
resolution = 8
output_file = "london_h3_grid_res8.gpkg"

gdf = gpd.read_file(input_file)
gdf = gdf.to_crs(epsg=4326)
gdf.geometry = gdf.geometry.buffer(0)

def polygon_to_h3(geom, res):
    cells = set()
    if geom.geom_type == "Polygon":
        exterior = [(lat, lng) for lng, lat in geom.exterior.coords]
        holes = [[(lat, lng) for lng, lat in ring.coords] for ring in geom.interiors]
        try:
            poly = LatLngPoly(exterior, holes)
            cells.update(h3.polygon_to_cells(poly, res))
        except:
            pass
    elif geom.geom_type == "MultiPolygon":
        for poly_geom in geom.geoms:
            exterior = [(lat, lng) for lng, lat in poly_geom.exterior.coords]
            holes = [[(lat, lng) for lng, lat in ring.coords] for ring in poly_geom.interiors]
            try:
                poly = LatLngPoly(exterior, holes)
                cells.update(h3.polygon_to_cells(poly, res))
            except:
                pass
    return cells

all_cells = set()
for geom in gdf.geometry:
    cells = polygon_to_h3(geom, resolution)
    all_cells.update(cells)

if len(all_cells) > 0:
    hexagons = []
    for cell in all_cells:
        boundary = h3.cell_to_boundary(cell)
        hexagon = Polygon([(lng, lat) for lat, lng in boundary])
        hexagons.append({"h3_id": cell, "geometry": hexagon})
        
    gdf_h3 = gpd.GeoDataFrame(hexagons, crs="EPSG:4326")
    gdf_h3.to_file(output_file, driver="GPKG")
    print(f"BAŞARILI! Dosya kaydedildi: {output_file}")
else:
    print("HATA: Altıgen üretilemedi.")