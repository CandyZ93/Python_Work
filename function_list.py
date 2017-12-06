'''
def greet_users(names):
	"""Greet to all the users in the list"""
	for name in names:
		msg =  "Hello, " + name.title() + '!'
		print(msg)
		
usernames = ['hannah', 'lance', 'kk lau',]
greet_users(usernames)

#printing_models
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron',]
completed_models = []

#print and move till no one left
while unprinted_designs:
	current_design = unprinted_designs.pop()
	
	#simulate the process
	print("Printing model: " + current_design)
	completed_models.append(current_design)
	
#print all the completed models--using for loop to print list
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)
	
'''
##homework
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	for n in range(len(magicians)):
		magicians[n] = "the great " + magicians[n]
	return magicians
		
def make_grater(magicians):
	tempMagis = []
	while magicians:
		tempMagis.append("the greter " + magicians.pop())
	tempMagis.reverse()
	for magi in tempMagis:
		magicians.append(magi)
	return magicians

		
magicians = ['david', 'john', 'lance', 'mike', ]

cmagi2 = make_great(magicians[:])
#cmagi = make_grater(magicians[:])

show_magicians(magicians)
show_magicians(cmagi2)
print(magicians)

