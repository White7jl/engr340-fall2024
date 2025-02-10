import numpy as np
import matplotlib.pyplot as plt
import os

# Define a list of file paths for your datasets
# Example: files = ["path_to_data1.csv", "path_to_data2.csv", "path_to_data3.csv"]
files = [
    "C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Documents/Acrylic Trial 1.csv",  # Replace with actual paths
    "C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Documents/Acrylic Trial 2.csv",
"C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Documents/Acrylic Trial 3.csv"
]

width = 4.52083  # inches
thickness = 0.102313  # inches
length = 2  # inches
area = 3.14*(thickness/2)**2  # in^2

# Loop through each dataset and process it
for file in files:
    # Load data into numpy (skip the first two rows and use comma as delimiter)
    data = np.loadtxt(file, skiprows=2, delimiter=",")

    # Slice each column
    time = data[:, 0]  # Time(s)
    load = data[:, 1]  # Load (lbf)
    extension = data[:, 2]  # Extension (in)

    # Calculate stress (lbf/in^2 or psi)
    stress = load / area  # in lbf/in^2 (psi)

    # Calculate strain (dimensionless)
    strain = extension / length


plt.plot(strain,strain,label="Stress-Strain Curve")
plt.plot(slope,strain,label="0.2% Offset Line")
plt.scatter(yield_stress,yield_strain,label="Yield Point")
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (psi)')
plt.title('Stress-Strain Curve w/ Offset Line')
plt.legend()
plt.show()