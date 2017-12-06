dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 400 can not assign tuple item

print("Origianl dimensions are:")
for dimension in dimensions:
	print(dimension)
	
dimensions=(400,10)
print("\nModified dimensions are:")
for dimension in dimensions:
	print(dimension)
