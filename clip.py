import pandas as pd
import numpy as np


# 读取数据并进行随机抽样
def read_and_sample_data(filepath, sample_frac=0.1):
    chunksize = 10 ** 6
    data = pd.DataFrame()
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        data = data.append(chunk.sample(frac=sample_frac))
    return data


# 保留在指定经纬度范围内的数据
def filter_data(data, ref_lat, ref_lon):
    filtered_data = data[(data['Lat (DD)'] >= ref_lat) & (data['Long (DD)'] >= ref_lon)]
    return filtered_data


def main():
    # CSV文件路径
    data_filepath = 'data/2015HI4178.csv'

    # 参考经纬度
    ref_lat = 0
    ref_lon = 50.74931

    # 读取并随机抽样数据
    print('Reading and sampling data...')
    data = read_and_sample_data(data_filepath, sample_frac=0.1)

    # 保留在指定经纬度范围内的数据
    print('Filtering data...')
    filtered_data = filter_data(data, ref_lat, ref_lon)

    # 保存过滤后的数据
    print('Saving filtered data...')
    filtered_data.to_csv('data/filtered_data.csv', index=False)

    print('Done.')


if __name__ == '__main__':
    main()

