import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 导入数据
data_path = "Data/CTD-Southease_230806231646_88104.xlsx"
data = pd.read_excel(data_path)
data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])

# 水位与温度
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['WaterLevel'], label='Water Level', color='blue')
plt.ylabel('Water Level')
plt.twinx()
plt.plot(data['TimeStamp'], data['Temperature'], label='Temperature', color='red')
plt.ylabel('Temperature')
plt.title('Water Level and Temperature vs Time')
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

# 盐度与电导率
plt.figure(figsize=(14, 4))
plt.plot(data['TimeStamp'], data['Salinity'], label='Salinity', color='purple')
plt.ylabel('Salinity')
plt.twinx()
plt.plot(data['TimeStamp'], data['Conductivity'], label='Conductivity', color='green')
plt.axhline(y=1, color='red', linestyle='-', linewidth=0.5)  # 电导率为1的红线
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