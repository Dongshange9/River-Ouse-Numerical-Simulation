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

# Set Timestamp as the index
filtered_arn_tides_data.set_index('Timestamp', inplace=True)

# Resample to 1-minute intervals and interpolate
resampled_data = filtered_arn_tides_data.resample('1T').asfreq()
interpolated_data = resampled_data.interpolate()

# Plot the interpolated Arun tides data
plt.figure(figsize=(16, 6))
plt.plot(interpolated_data.index, interpolated_data['Tide_OD'], marker='', linestyle='-', linewidth=1)
plt.xlabel('Timestamp')
plt.ylabel('Tide Height (m)')
plt.title('Interpolated Arun Tides Data for July 2023 (1-minute intervals)')
plt.grid(True)
plt.show()



# Identify local maxima
local_maxima = interpolated_data[
    (interpolated_data['Tide_OD'] > interpolated_data['Tide_OD'].shift(1)) &
    (interpolated_data['Tide_OD'] > interpolated_data['Tide_OD'].shift(-1))
]

# Print timestamps of local maxima
print("Timestamps of local maxima:")
print(local_maxima.index)
