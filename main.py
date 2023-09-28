# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('data/2015HI1477N.csv')

# 设置随机种子，保证结果的可复现性
np.random.seed(0)

# 随机生成一个布尔型数组，数组长度与 df 的行数相同
# np.random.rand(len(df)) 生成一个与 df 行数相同的在[0, 1)范围内均匀分布的随机数组
# 将其与 0.1 比较，生成一个布尔型数组，True 的概率约为 10%
mask = np.random.rand(len(df)) <= 0.1

# 保留随机选取的约 10% 的行
df_thinned = df[mask]

# 将结果保存为新的 CSV 文件
df_thinned.to_csv('data/2015HI1477N-Thin.csv', index=False)

print("Done. The thinned data is saved as '2015-HI_thinned.csv' in the 'data' folder.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
