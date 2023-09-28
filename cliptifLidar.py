from osgeo import gdal
import os


def tif_to_xyz(input_file, output_file):
    ds = gdal.Open(input_file)
    band = ds.GetRasterBand(1)

    transform = ds.GetGeoTransform()
    x_origin = transform[0]
    y_origin = transform[3]
    pixel_width = transform[1]
    pixel_height = transform[5]

    data = band.ReadAsArray()
    rows, cols = data.shape

    with open(output_file, 'w') as f:
        for row in range(rows):
            for col in range(cols):
                x = x_origin + col * pixel_width
                y = y_origin + row * pixel_height
                val = data[row, col]
                if val != band.GetNoDataValue():  # Exclude NoData values
                    f.write(f"{x} {y} {val}\n")

    print(f"Conversion completed. Data saved to {output_file}.")


if __name__ == '__main__':
    input_path = os.path.join("data", "input.tif")
    output_path = os.path.join("data", "output.xyz")

    tif_to_xyz(input_path, output_path)