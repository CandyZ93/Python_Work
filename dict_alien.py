alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

'''print(alien_0)

alien_1 = {}

print(alien_1)

alien_1['xx'] = 1
alien_1['yy'] = 2

print(alien_1)

print("The color of the alien is "+alien_0['color']+"!")
alien_0['color'] = 'yellow'
print("The color of the alien is "+alien_0['color']+"!")

del alien_0['points']
print(alien_0)'''

favorite_languages = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'python',
	}
	
print(favorite_languages)

print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")

for key, value in alien_0.items():
	print("\nKey: " + key+'.')
	print("Value: " + str(value)+'.')
	


