import pyart  # Import the Py-ART library for radar data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import pooch  # Import pooch for data fetching
import numpy as np  # Import numpy for numerical operations
import matplotlib  # Import matplotlib to configure the plotting backend

# Set the matplotlib backend to 'Agg' for non-GUI environments or 'TkAgg' if you need a GUI backend
# 'Agg' is used for script-based plotting without an interactive window
matplotlib.use('Agg')

# Correct MD5 hash obtained from a previous validation step
correct_md5_hash = "64caf070f295534d312fea75b0bcb888"

# Create a pooch instance to manage the dataset fetching
DATASETS = pooch.create(
    # Cache path for storing the downloaded file
    path=pooch.os_cache("open-radar-data"),
    # Base URL to fetch the dataset
    base_url="https://github.com/openradar/open-radar-data/raw/main/data/",
    registry={
        # File name and its MD5 hash for validation
        "sample_sgp_data.nc": f"md5:{correct_md5_hash}",
    },
)

# Fetch the radar data file
filepath = DATASETS.fetch("sample_sgp_data.nc")

# Read the radar data from the file using Py-ART
radar = pyart.io.read(filepath)

# Print the available radar data fields to understand what is in the file
print("Available fields:", radar.fields.keys())

# Print various metadata and data attributes from the radar object
print(radar.time)       # Time of the radar data
print(radar.range)      # Radar range data
print(radar.fields)     # Dictionary containing different radar fields
print(radar.metadata)   # Metadata associated with the radar data
print(radar.scan_type)  # Type of radar scan used (e.g., PPI, RHI)
print(radar.latitude)   # Latitude of the radar's location
print(radar.longitude)  # Longitude of the radar's location
print(radar.altitude)   # Altitude of the radar's location

# Define the field name to be visualized (assumed to be 'reflectivity_horizontal')
field_name = 'reflectivity_horizontal'

# Create a RadarDisplay object for visualizing radar data
display = pyart.graph.RadarDisplay(radar)

# Plot the reflectivity field from the first sweep of the radar data
plt.figure(figsize=(10, 8))  # Create a figure with a specified size
display.plot(field_name, 0)  # Plot the specified field from the first sweep
# Set the limits for x and y axes
display.set_limits(xlim=(-150, 150), ylim=(-150, 150))
plt.title("Reflectivity Field (First Sweep)")  # Set the title of the plot
# Save the plot to a file
plt.savefig('/home/meetb/Downloads/radar_reflectivity.png')
plt.close()  # Close the plot to free up memory

# Additional Analysis

# 1. Visualize Multiple Fields
fields_to_plot = ['reflectivity_horizontal', 'velocity',
                  'differential_reflectivity']  # List of fields to plot

for field in fields_to_plot:
    if field in radar.fields:  # Check if the field exists in the radar data
        plt.figure(figsize=(10, 8))  # Create a figure with a specified size
        display.plot(field, 0)  # Plot the specified field from the first sweep
        # Set the limits for x and y axes
        display.set_limits(xlim=(-150, 150), ylim=(-150, 150))
        # Set the title of the plot
        plt.title(f"{field.capitalize()} Field (First Sweep)")
        # Save the plot to a file
        plt.savefig(f'/home/meetb/Downloads/radar_{field}.png')
        plt.close()  # Close the plot to free up memory

# 2. Analyze Multiple Sweeps
for sweep in range(radar.nsweeps):  # Iterate through each sweep in the radar data
    plt.figure(figsize=(10, 8))  # Create a figure with a specified size
    # Plot the reflectivity field for the current sweep
    display.plot('reflectivity_horizontal', sweep)
    # Set the limits for x and y axes
    display.set_limits(xlim=(-150, 150), ylim=(-150, 150))
    # Set the title of the plot
    plt.title(f"Reflectivity Field (Sweep {sweep})")
    # Save the plot to a file
    plt.savefig(f'/home/meetb/Downloads/radar_reflectivity_sweep_{sweep}.png')
    plt.close()  # Close the plot to free up memory

# 3. Statistical Summary of Reflectivity
# Extract the data for the reflectivity field
reflectivity = radar.fields['reflectivity_horizontal']['data']

# Calculate statistical metrics for reflectivity
mean_reflectivity = np.mean(reflectivity)  # Mean value of the reflectivity
max_reflectivity = np.max(reflectivity)  # Maximum value of the reflectivity
min_reflectivity = np.min(reflectivity)  # Minimum value of the reflectivity
# Standard deviation of the reflectivity
std_reflectivity = np.std(reflectivity)

# Print the statistical summary
print(f"Reflectivity Statistics:")
print(f"Mean: {mean_reflectivity}")
print(f"Max: {max_reflectivity}")
print(f"Min: {min_reflectivity}")
print(f"Standard Deviation: {std_reflectivity}")

# 4. Histogram of Reflectivity
plt.figure(figsize=(10, 8))  # Create a figure with a specified size
# Create a histogram of reflectivity values
plt.hist(reflectivity.flatten(), bins=50, color='blue', alpha=0.7)
plt.title('Histogram of Reflectivity')  # Set the title of the histogram
plt.xlabel('Reflectivity (dBZ)')  # Set the x-axis label
plt.ylabel('Frequency')  # Set the y-axis label
plt.grid(True)  # Add grid lines to the histogram
# Save the histogram plot to a file
plt.savefig('/home/meetb/Downloads/histogram_reflectivity.png')
plt.close()  # Close the plot to free up memory

# 5. Generate Composite Reflectivity
# Generate a Cartesian grid from the radar data for composite reflectivity visualization
grid = pyart.map.grid_from_radars(
    radar,
    # Define the shape of the grid (1 sweep, 500x500 grid)
    grid_shape=(1, 500, 500),
    # Define grid limits (range and coordinates)
    grid_limits=((0, 10000), (-150000, 150000), (-150000, 150000)),
    fields=[field_name]  # Field to be included in the grid
)

# Retrieve the data from the grid and remove extra dimensions
# Get the data and remove the first dimension
composite_reflectivity = grid.fields[field_name]['data'][0]

# Ensure the data is 2D
if composite_reflectivity.ndim == 1:
    composite_reflectivity = np.reshape(
        composite_reflectivity, (500, 500))  # Reshape to 2D if necessary

# Plot the composite reflectivity data
plt.figure(figsize=(10, 8))  # Create a figure with a specified size
plt.imshow(composite_reflectivity, cmap='pyart_Carbone42',
           extent=(-150, 150, -150, 150))  # Display the image with a color map
plt.colorbar(label='Reflectivity (dBZ)')  # Add a color bar with label
plt.title('Composite Reflectivity')  # Set the title of the plot
plt.xlabel('Distance (km)')  # Set the x-axis label
plt.ylabel('Distance (km)')  # Set the y-axis label
plt.grid(True)  # Add grid lines to the plot
# Save the composite reflectivity plot to a file
plt.savefig('/home/meetb/Downloads/composite_reflectivity.png')
plt.close()  # Close the plot to free up memory
