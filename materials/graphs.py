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


# Geometry and material properties (same for all datasets)
width = 4.52083  # inches
thickness = 0.102313  # inches
length = 2  # inches

# Geometry and material properties (same for all datasets)
width_r = 4.52083  # inches
thickness_r = 0.102313  # inches
length_r = 2  # inches
area_r = 3.14*(thickness/2)**2  # in^2

# Initialize the plot
plt.figure(figsize=(10, 6))

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

    # Plot the stress-strain curve for the current dataset
    plt.plot(stress, strain, label=f"Dataset: {os.path.basename(file)}")

# Labels and title for the plot
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (ksi)')
plt.title('Stress-Strain Curves of All Specimen')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
