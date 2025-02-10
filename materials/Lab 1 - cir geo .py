import numpy as np
import matplotlib.pyplot as plt

#path to overall file
path_to_file = "C:/Users/jasmi/OneDrive - James Madison University (Dukes)/Documents/Copper Trial 1.csv"
#load data into numpy
data = np.loadtxt(path_to_file, skiprows=2, delimiter=",")
#print(data)

#slice each column to a list
time = data[:,0]                   #Time(s)
load = data[:,1]                   #load(lbf),Load = amount of force
extension = data[:,2]              #extension(in),the change in length

#create variable to hold the given info
##geometry rectangular & material is wood
#variables are in inches
width = 5
thickness = 0.10259
length = 2

#Find area we know that the shape is circular
area = (3.14*(thickness/2))**2        #in in^2

#use area t0 find stress
stress = load/area             #in lbf/in^2 (psi)

#use the extension (change in length) and length to find strain
strain = extension/length           #no units(dimensionless)

#Tensile Strength aka Ultimate Strength
utl_stress = max(stress)
print("This is the tensile stress",utl_stress)
ult_strain =max(strain)
print("This is the tensile strain", ult_strain)

#now we can create the stress-strain diagram
plt.plot(stress,strain,label="Stress-Strain Graph")
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (psi)')
plt.title('Stress-Strain Curve')
plt.legend()
plt.show()

offset = 0.002

#Modulus of Elasticity
elastic_region = 10                     #Elastic zone stops at 10 (refer to graph 1)
delta_stress = np.diff(stress[:10])     #change in stress
delta_strain = np.diff(strain[:10])     #change in strain
E = np.mean(delta_stress/delta_strain)

#Yield Strength
slope = (E*strain)-offset               #find slope use minus sign to shift right
yield_pt = np.argmax(stress >= slope)   #call out yield point
yield_stress = stress[yield_pt]         #find stress at yield point
yield_strain = strain[yield_pt]         #find strain at yield point

#Modulus of Resilience
Ur = np.trapz(stress[:yield_pt],strain[:yield_pt])  #use np.trapz to take area under curve up to yield point

#Modulus of Toughness
MT = np.trapz(stress,strain)    #use np.trapz to take area under curve up to breaking point

#Duclity
pE = (extension[-1]/length)*100
print("This is percent elongation",pE)
fracture_stress = stress[-1]
fracture_area  = load[-1]/fracture_stress
pR =((area-fracture_area)/area)*100
print("this is percent reduction in area", pR)

#now we can create the stress-strain diagram w/ offset line and yield point
plt.plot(stress,strain,label="Stress-Strain Curve")
plt.plot(slope,strain,label="0.2% Offset Line")
plt.scatter(yield_stress,yield_strain,label="Yield Point")
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (psi)')
plt.title('Stress-Strain Curve w/ Offset Line')
plt.legend()
plt.show()

"First, I imported data from the csv file and defined the given variables. Using the given thickness and width I"
"I determined area. Then I used the load data and the area to determine stress and used the extension data and "
"length to determine strength. Once I had those things I could create a stress-strain graph by plotting the stress"
"and strain data by using the strain equation. Once I had stress and strain I plotted them. Next, I determined the"
"modulus of elasticity by taking the change in stress over the change in strain.Then I determine the yield point."
"I find the slope using y = mx+b and identify the yield strength based on the intersection of the offset line and"
"stress-strain curve aka 0.2% method. Finally I determine the modulus of toughness and resilience by taking the area"
"under the curve to there respective points. I created a graph for the stress-strain curve and offset line and"
"identified the yield point.I printed all the answers below."

print("This is the yield strength",yield_pt,"psi")
print("This is the Modulus of elasticity", E, "psi")
print("This is the Modulus of Toughness", MT, "psi")
print("This is the Modulus of Resilience", Ur, "psi")

