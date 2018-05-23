# Established showroom
showroom = set(['Chevy Volt', 'Cadillac CTS', 'GMC Yukon', 'Nissan Xterra'])
print('My cars')
print(showroom)

# adding cars to sets
showroom.update(['GMC Denali', 'Maserati Quattroporte'])
print('Added a car to the showroom')
print(showroom)

# removing car from set
showroom.discard('Chevy Volt')
print('Removed the Chevy from the showroom')
print(showroom)

# established junkyard set
junkyard = set(['Chevy Iroc-Z', 'GMC Yukon', 'Potiac Fiero', 'Nissan Xterra'])
print('My Junkyard')
print(junkyard)

# which cars are in both?
print('Same Cars')
print(junkyard.intersection(showroom))

# joining all the cars
print('Union of Cars')
print(showroom.union(junkyard))

# remove cars from list
def removeCars(cars):
  cars.remove("Cadillac CTS")
  print('removed the caddy')
  print(cars)
removeCars(showroom.union(junkyard))