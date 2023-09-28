import pandas as pd
import matplotlib.pyplot as plt

# Load the data without specifying date parsing
arn_tides_data = pd.read_csv("Data/Arn_tides202307.txt", delimiter='\t')

# Manually parse the 'Date/Time (GMT)' column to datetime
arn_tides_data['Date/Time (GMT)'] = pd.to_datetime(arn_tides_data['Date/Time (GMT)'], errors='coerce')

# Rename the timestamp column for easier handling
arn_tides_data.rename(columns={'Date/Time (GMT)': 'Timestamp'}, inplace=True)

# Filter out the exceptional values (9999)
filtered_arn_tides_data = arn_tides_data[arn_tides_data['Tide_OD'] != 9999]

# Plot the filtered Arun tides data
plt.figure(figsize=(16, 6))
plt.plot(filtered_arn_tides_data['Timestamp'], filtered_arn_tides_data['Tide_OD'], marker='o', linestyle='-', linewidth=1, markersize=3)
plt.xlabel('Timestamp')
plt.ylabel('Tide Height (m)')
plt.title('Filtered Arun Tides Data for July 2023')
plt.grid(True)
plt.show()




