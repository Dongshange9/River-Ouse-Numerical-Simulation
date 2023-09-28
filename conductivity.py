import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. 导入数据
data_path = "Data/CTD-Southease_230806231646_88104.xlsx"
data = pd.read_excel(data_path)
data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])

# 2. 绘制初始图形
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['Conductivity'], label='Conductivity', color='green')
plt.ylabel('Conductivity')
plt.title('Conductivity vs Time')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.show()

# 3. 查找6月22日23点左右的局部最低值
local_min_date = pd.Timestamp('2023-06-22 23:00')
time_window = pd.Timedelta(hours=1)  # 1 hour window to find the local minimum
local_min_value = data[(data['TimeStamp'] >= local_min_date - time_window) &
                       (data['TimeStamp'] <= local_min_date + time_window)]['Conductivity'].min()
print(f"Local minimum conductivity value around 22nd June 23:00 is: {local_min_value}")

# 4. 删除6月23日到6月29日出现的比该值低的值
start_date = pd.Timestamp('2023-06-23 00:00')
end_date = pd.Timestamp('2023-06-29 23:59')
data.loc[(data['TimeStamp'] >= start_date) &
         (data['TimeStamp'] <= end_date) &
         (data['Conductivity'] < local_min_value), 'Conductivity'] = None

# 5. 删除所有1以下的电导率值
data.loc[data['Conductivity'] < 1, 'Conductivity'] = None

# 6. 删除6月27日的最低值
min_date_27 = pd.Timestamp('2023-06-27 00:00')
max_date_27 = pd.Timestamp('2023-06-27 23:59')
min_value_27 = data[(data['TimeStamp'] >= min_date_27) & (data['TimeStamp'] <= max_date_27)]['Conductivity'].min()
data.loc[(data['TimeStamp'] >= min_date_27) & (data['TimeStamp'] <= max_date_27) & (data['Conductivity'] == min_value_27), 'Conductivity'] = None
# 删除6月30日的最低值
min_date_30 = pd.Timestamp('2023-06-30 00:00')
max_date_30 = pd.Timestamp('2023-06-30 23:59')
min_value_30 = data[(data['TimeStamp'] >= min_date_30) & (data['TimeStamp'] <= max_date_30)]['Conductivity'].min()
data.loc[(data['TimeStamp'] >= min_date_30) & (data['TimeStamp'] <= max_date_30) & (data['Conductivity'] == min_value_30), 'Conductivity'] = None

# 7. 使用线性插值来连接断开的地方
data['Conductivity'] = data['Conductivity'].interpolate(method='linear')


# 8. 绘制处理后图形
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['Conductivity'], label='Conductivity', color='green')
plt.axhline(y=1, color='red', linestyle='-', linewidth=0.5)  # 电导率为1的红线
plt.ylabel('Conductivity')
plt.title('Conductivity vs Time (With Specific Values Removed)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.show()


# 盐度与电导率
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['Salinity'], label='Salinity', color='purple')
plt.ylabel('Salinity')
plt.twinx()
plt.plot(data['TimeStamp'], data['Conductivity'], label='Conductivity', color='green')

plt.ylabel('Conductivity')
plt.title('Salinity and Conductivity vs Time')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.show()

# 电导率与温度
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['Conductivity'], label='Conductivity', color='green')
plt.ylabel('Conductivity')
plt.twinx()
plt.plot(data['TimeStamp'], data['Temperature'], label='Temperature', color='red')
plt.ylabel('Temperature')
plt.title('Conductivity and Temperature vs Time')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.show()

# 水位与电导率
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['WaterLevel'], label='Water Level', color='blue')
plt.ylabel('Water Level')
plt.twinx()
plt.plot(data['TimeStamp'], data['Conductivity'], label='Conductivity', color='green')
plt.axhline(y=1, color='red', linestyle='-', linewidth=0.5)  # 电导率为1的红线
plt.ylabel('Conductivity')
plt.title('Water Level and Conductivity vs Time')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.show()
