import os
from osgeo import gdal


def shp_to_asc(input_shp, output_asc, pixel_size=2.0):
    # 创建临时GeoTIFF文件
    temp_tif = os.path.join(os.path.dirname(output_asc), "temp.tif")

    # 从shapefile获取范围
    ds = gdal.OpenEx(input_shp)
    layer = ds.GetLayer()
    x_min, x_max, y_min, y_max = layer.GetExtent()

    x_res = int((x_max - x_min) / pixel_size)
    y_res = int((y_max - y_min) / pixel_size)

    # 转换到临时GeoTIFF
    gdal_cmd = f"gdal_rasterize -l {os.path.basename(input_shp)[:-4]} -burn 0.0 -ts {x_res} {y_res} -a_nodata 0.0 -ot Float32 -of GTiff {input_shp} {temp_tif}"
    os.system(gdal_cmd)

    # 转换到AAIGrid
    gdal_translate_cmd = f"gdal_translate -of AAIGrid {temp_tif} {output_asc}"
    os.system(gdal_translate_cmd)

    # 删除临时文件
    os.remove(temp_tif)


def tif_to_asc(input_tif, output_asc):
    gdal_cmd = f"gdal_translate -of AAIGrid {input_tif} {output_asc}"
    os.system(gdal_cmd)


data_dir = 'data'
input_files = ['seabed_input.shp', 'riverbed_input.tif']

for input_file in input_files:
    input_path = os.path.join(data_dir, input_file)
    output_path = os.path.join(data_dir, input_file.split('.')[0] + '.asc')

    if input_file.endswith('.shp'):
        shp_to_asc(input_path, output_path)
    elif input_file.endswith('.tif'):
        tif_to_asc(input_path, output_path)
