import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook
from bokeh.models import HoverTool

# Load the dataset
df = pd.read_csv('C:/Users/Admin/Desktop/delhiaqi.csv', parse_dates=['date'])

# Display basic information about the dataset
print(df.info())
print(df.describe())

# Descriptive statistics
print(df.describe())

# Calculate the correlation matrix
corr = df[['co', 'no2', 'o3', 'pm2_5', 'pm10', 'nh3']].corr()

# Create a heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Between Pollutants')
plt.show()

# Plot the distribution of each pollutant
plt.figure(figsize=(12, 8))
for i, column in enumerate(['co', 'no2', 'o3', 'pm2_5', 'pm10', 'nh3']):
    plt.subplot(2, 3, i+1)
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(f'Distribution of {column}')
plt.tight_layout()
plt.show()

# Activate output in the notebook
output_notebook()

# Create the Bokeh plot
p = figure(x_axis_type='datetime', title="Pollutants Over Time", width=800, height=400)
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Concentration (µg/m³)'

# Add lines for pollutants with hover tool
pollutants = ['CO', 'NO2', 'O3', 'PM2_5', 'PM10', 'NH3']
colors = ['blue', 'green', 'orange', 'red', 'purple', 'brown']
for pollutant, color in zip(pollutants, colors):
    p.line(df['date'], df[pollutant], legend_label=pollutant, line_width=2, color=color)

p.add_tools(HoverTool())
p.legend.location = "top_left"

# Show the plot
show(p)

