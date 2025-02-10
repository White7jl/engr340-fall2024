import numpy as np
import matplotlib.pyplot as plt

# Path to overall file
path_to_file = "C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Documents/High Carbon Trial 1.csv"
# Load data into mumpy
data = np.loadtxt(path_to_file, skiprows=2, delimiter=",")

# Slice each column to a list
time = data[:, 0]  # Time(s)
load = data[:, 1]  # Load (lbf)
extension = data[:, 2]  # Extension (in)

# Geometry (circular cross-section)
width = 6.5  # inches
thickness = 0.0004  # inches
length = 2  # inches

# Find area (circular cross-section)
area = (3.14 * (thickness / 2)) ** 2  # in^2

# Calculate stress (lbf/in^2 or psi)
stress = load / area  # in lbf/in^2 (psi)

# Calculate strain (dimensionless)
strain = extension / length

# Tensile Strength (Ultimate Strength)
utl_stress = max(stress)
print("This is the tensile stress", utl_stress)
ult_strain = max(strain)
print("This is the tensile strain", ult_strain)

# Now we can create the stress-strain diagram
plt.plot(stress, strain, label="Stress-Strain Graph")
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (ksi)')
plt.title('Stress-Strain Curve')
plt.legend()
plt.show()

# Modulus of Elasticity (E) - Linear region assumed from start to 10% strain
elastic_region_end = 10  # Elastic region stops at 10% strain
elastic_limit = strain <= (elastic_region_end / 100)
delta_stress = np.diff(stress[elastic_limit])  # Change in stress
delta_strain = np.diff(strain[elastic_limit])  # Change in strain
E = np.mean(delta_stress / delta_strain)  # Modulus of elasticity

# Yield Strength (0.2% Offset)
offset = 0.002
slope = E * strain - offset  # Offset line equation

# Find the yield point by finding the intersection of the offset line and stress-strain curve
yield_pt = np.argmax(stress >= slope)  # Find the index where stress is greater than the offset line
yield_stress = stress[yield_pt]  # Stress at yield point
yield_strain = strain[yield_pt]  # Strain at yield point

# Modulus of Resilience
Ur = np.trapz(stress[:yield_pt], strain[:yield_pt])  # Area under curve up to yield point

# Modulus of Toughness
MT = np.trapz(stress, strain)  # Area under curve up to fracture


# Ductility: Percent Elongation and Percent Reduction in Area
pE = (extension[-1] / length) * 100  # Percent elongation
print("This is percent elongation", pE)

fracture_stress = stress[-1]
fracture_area = load[-1] / fracture_stress  # Approximate area at fracture
pR = ((area - fracture_area) / area) * 100  # Percent reduction in area
print("This is percent reduction in area", pR)

# Now we can create the stress-strain diagram with the offset line and yield point
plt.plot(stress, strain, label="Stress-Strain Curve")
plt.plot(strain, slope, label="0.2% Offset Line", linestyle='--')  # Offset line (dashed)
plt.scatter(yield_strain, yield_stress, label="Yield Point", color='red')
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (psi)')
plt.title('Stress-Strain Curve w/ Offset Line')
plt.legend()
plt.show()

print("This is the yield strength", yield_stress, "psi")
print("This is the Modulus of Elasticity", E, "psi")
print("This is the Modulus of Toughness", MT, "psi")
print("This is the Modulus of Resilience", Ur, "psi")
