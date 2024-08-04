# Radar Data Analysis
This project performs radar data analysis using Py-ART, a Python library for weather radar data processing and visualization. The code demonstrates how to fetch radar data, visualize various fields, and perform statistical analysis and plotting.

## Table of Contents :
1.Overview
Requirements
Setup
Usage
Results
License

# Overview:
This script fetches radar data from a remote source, reads it using the Py-ART library, and performs several analyses including:

Field Visualization: Plots various radar fields.
Sweep Analysis: Visualizes data from multiple radar sweeps.
Statistical Summary: Computes and prints statistical metrics for reflectivity.
Histogram Plot: Creates a histogram of reflectivity values.
Composite Reflectivity: Generates and saves a composite reflectivity plot.

# Requirements:
To run this code, you'll need the following Python packages:

pyart - For radar data manipulation.
matplotlib - For plotting graphs.
pooch - For data fetching and caching.
numpy - For numerical operations.
You can install these packages using pip:

bash
pip install pyart matplotlib pooch numpy

# Setup:
Clone the Repository:

bash
git clone https://github.com/your-username/radar-analysis.git
cd radar-analysis
Create a Virtual Environment (Optional but recommended):

bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Requirements:

bash
pip install pyart matplotlib pooch numpy

Usage : 

Run the Script:

Save the provided Python code into a file named radar_analysis.py in your project directory. Execute the script using:

bash

python radar_analysis.py

Check the Outputs:

Plots: The script saves various plots to the /home/meetb/Downloads/ directory. Adjust the paths if necessary.
Statistical Summary: The script prints statistical metrics for the reflectivity field to the console.

# Results:
The script generates the following outputs:

Reflectivity Field (First Sweep): radar_reflectivity.png
Visualizations for Multiple Fields: radar_reflectivity_horizontal.png, radar_velocity.png, radar_differential_reflectivity.png
Sweeps Analysis: radar_reflectivity_sweep_X.png (where X is the sweep number)
Histogram of Reflectivity: histogram_reflectivity.png
Composite Reflectivity: composite_reflectivity.png

# License :
This project is licensed under the MIT License. See the LICENSE file for details.

