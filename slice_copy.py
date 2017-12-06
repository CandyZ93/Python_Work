my_foods=['beef', 'shrimp', 'crab']
friend_foods=my_foods[:]

my_foods.append('banana')
print(friend_foods)
print(my_foods)
friend_foods.append('coconut')
print(friend_foods)
print(my_foods)

print("\nThe last three items are:")
for food in my_foods[-3:]:
	print(food)
