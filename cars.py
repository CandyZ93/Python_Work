cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort(reverse=True)
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list agian:")
print(cars)
cars.reverse()
print(cars)
print(len(cars))

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
		
flag='subaru' in cars
print(flag)

if 'citroen' not in cars:
	cars.append('citroen')
print(cars)

