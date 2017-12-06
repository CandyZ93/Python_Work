magicians = ['alice', 'david', 'lance']
for magician in magicians:
	print(magician.title()+", that was a great trick!")
	print("Can't wait to see your next trick, " +magician.title()+"!\n")
	
print("Thank you, everyone. That was a great magic show!") 

for value in range(10):
	print(value)

digits = list(range(1,11,2))
print(digits)
print(sum(digits))

cubes=[value**3 for value in range(1,11)]
print(cubes)

million=list(range(1,1000001))
print(min(million))
print(max(million))
#print(sum(million))

threetimes = list(range(3,31,3))
for n_three in threetimes:
	print(n_three)

#slice

numbers=list(range(1,11))
print(numbers[:3])
print(numbers[1:4])
print(numbers[2:])
print(numbers[-1:])
print(numbers[-3:])

for n in numbers[-3:]:
	print(n)
