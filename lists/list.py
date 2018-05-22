planets = ["Mercury", "Mars"]
print('Planets to start with')
print(planets)

planets.append('Jupiter')
planets.append('Saturn')
print('Appended planet list')
print(planets)

planets.extend(['Uranus', 'Neptune'])
print('Planets extended')
print(planets)

planets.insert(1, 'Venus')
planets.insert(2, 'Earth')
print('Planets Inserted?')
print(planets)

planets.append('Pluto')
print('Pluto added to list')
print(planets)

rockey_planets = planets[slice(0,4)]
print('rocky planets')
print(rockey_planets)

# planets.pop()
del planets[8]
print('Pluto deleted')
print(planets)

satellites = [('sat1', 'Mars'), ('sat2', 'Mars'), ('sat3', 'Earth'), ('sat4', 'Jupiter'),('sat5', 'Jupiter')]

def satCheck(planets, sats):
  print("Planets that had a satellite fly by")
  for planet in planets:
    for sat in sats:
      if planet == sat:
        print(f"{planet} : {sat[0]}")
satCheck(planets,satellites)