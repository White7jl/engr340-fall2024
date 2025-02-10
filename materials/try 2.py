import numpy as np
import matplotlib.pyplot as plt


def calculate_stress_strain(load, extension, area, original_length):
    # Calculate strain and stress arrays
    strain = extension / original_length
    stress = load / area
    return strain, stress


def offset_line(E, offset_strain, strain_values):
    # The offset line equation is: sigma = E * (epsilon - offset_strain)
    return E * (strain_values - offset_strain)


def find_intersection(strain_values, stress_values, offset_strain, E):
    # Calculate the offset line
    offset_stress_values = offset_line(E, offset_strain, strain_values)

    # Find the point of intersection where stress from the curve crosses the offset line
    for i in range(1, len(strain_values)):
        if stress_values[i] > offset_stress_values[i] and stress_values[i - 1] < offset_stress_values[i - 1]:
            # Intersection point found, return the stress at the intersection
            intersection_stress = stress_values[i]
            return intersection_stress, strain_values[i]
    return None, None


def calculate_yield_point(path_to_file, offset_strain=0.002):
    # Load data from the CSV file
    data = np.loadtxt(path_to_file, skiprows=2, delimiter=",")

    # Slice each column to a list
    time = data[:, 0]  # Time (s)
    load = data[:, 1]  # Load (lbf)
    extension = data[:, 2]  # Extension (in)

    # Geometry and material properties
    width = 6.5  # in inches (example, adjust as needed)
    thickness = 0.0004  # in inches (example, adjust as needed)
    original_length = 2  # in inches (example, adjust as needed)
    E = 14021172.36347  # Young's Modulus (psi) for wood (adjust as needed)

    # Calculate the cross-sectional area (in^2)
    area = width * thickness

    # Calculate the stress-strain curve
    strain_values, stress_values = calculate_stress_strain(load, extension, area, original_length)

    # Find the yield point using the offset method (0.2% offset)
    intersection_stress, intersection_strain = find_intersection(strain_values, stress_values, offset_strain, E)

    # Plot the stress-strain curve and the offset line
    plt.figure(figsize=(8, 6))
    plt.plot(strain_values, stress_values, label="Stress-Strain Curve", color='blue')
    plt.plot(strain_values, offset_line(E, offset_strain, strain_values), label="Offset Line (0.2%)", linestyle='--',
             color='red')

    if intersection_stress is not None:
        plt.scatter(intersection_strain, intersection_stress, color='green',
                    label=f"Yield Point: {intersection_stress:.2f} psi")

    plt.xlabel("Strain (dimensionless)")
    plt.ylabel("Stress (psi)")
    plt.title("Stress-Strain Curve and Yield Point (0.2% Offset Method)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Return the yield point stress and strain
    if intersection_stress is not None:
        return intersection_stress, intersection_strain
    else:
        print("No intersection found.")
        return None, None


# Example usage:
path_to_file = "C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Documents/High Carbon Trial 1.csv"
yield_stress, yield_strain = calculate_yield_point(path_to_file)
if yield_stress is not None:
    print(f"Yield Point Stress (0.2% offset method): {yield_stress:.2f} psi")
    print(f"Yield Point Strain (0.2% offset method): {yield_strain:.4f}")
