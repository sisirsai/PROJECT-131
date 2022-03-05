import pandas as pd
import csv

df = pd.read_csv('data.csv')

df['Mass'] = 1.989e+8*df['Mass']
df['Radius'] = 6.957e+8*df['Radius']

df.to_csv('new_data.csv')

rows = []

with open("data.csv", "r") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    rows.append(row)

planet_data = rows[1:]

planet_masses = []
planet_radii = []
planet_names = []

for planetd in planet_data:
  planet_masses.append(planetd[3])
  planet_radii.append(planetd[4])
  planet_names.append(planetd[1])

def find_gravity(mass,radius):
    return (6.67*10**-11*mass)/radius**2

planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = find_gravity(float(planet_masses[index]) , float(planet_radii[index]))
  planet_gravity.append(gravity)

planet_gravity.insert(0,'Acceleration due to Gravity on this Planet')

final_data = pd.DataFrame(rows)
final_data[7] = planet_gravity

del final_data[0]
final_data.to_csv('Final_data.csv')