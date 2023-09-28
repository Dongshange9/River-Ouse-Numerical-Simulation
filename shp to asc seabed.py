
import os
from osgeo import gdal, ogr

def shp_to_tif(input_shp, output_tif, pixel_size=1):
    # Open the data source
    source_ds = ogr.Open(input_shp)
    source_layer = source_ds.GetLayer()

    # Create the destination raster data source
    x_min, x_max, y_min, y_max = source_layer.GetExtent()
    x_res = int((x_max - x_min) / pixel_size)
    y_res = int((y_max - y_min) / pixel_size)

    target_ds = gdal.GetDriverByName('GTiff').Create(output_tif, x_res, y_res, 1, gdal.GDT_Float32)
    target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
    band = target_ds.GetRasterBand(1)
    band.SetNoDataValue(-9999)

    # Rasterize
    gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

def tif_to_asc(input_tif, output_asc):
    # Convert tif to asc
    gdal.Translate(output_asc, input_tif, format="AAIGrid")

def main():
    input_shp = "Data/seabed_input.shp"
    temp_tif = "Data/seabed_output_temp.tif"
    output_asc = "Data/seabed_output.asc"

    # Convert shapefile to tif
    shp_to_tif(input_shp, temp_tif)

    # Convert tif to asc
    tif_to_asc(temp_tif, output_asc)

    # Optionally remove the temporary tif file
    os.remove(temp_tif)

if __name__ == "__main__":
    main()
