from osgeo import gdal, ogr

# 输入和输出文件
input_shp = 'G:\\dissertation\\0908\\09083\\合并研究区.shp'
output_raster = 'G:\\dissertation\\0908\\合并研究区.tif'
field_name = "Depth"  # Shapefile中您希望插值的字段名

# 打开shapefile
source_ds = ogr.Open(input_shp)
if not source_ds:
    raise ValueError("Failed to open the shapefile. Please check the file path and integrity.")

source_layer = source_ds.GetLayer()

# 创建输出栅格的范围和分辨率
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# 输出栅格的分辨率
pixel_size = 2  # 2米
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)

# 创建新的栅格数据集
target_ds = gdal.GetDriverByName('GTiff').Create(output_raster, x_res, y_res, 1, gdal.GDT_Float32)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(-9999)

# 使用gdal.RasterizeLayer将矢量层栅格化到新的数据集中
gdal.RasterizeLayer(target_ds, [1], source_layer, options=["ATTRIBUTE=" + field_name])

# 关闭数据集
source_ds = None
target_ds = None
