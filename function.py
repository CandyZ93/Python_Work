'''
def describe_pet(pet_name, animal_type = 'dog'):
    """display pet's infomation"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " +
          pet_name.title() + ".")

describe_pet('tom', 'hamster')
describe_pet('dog', 'harry' )
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet('john')
describe_pet('john', 'fish')

##--home work 8.1-5
def make_shirt(size, words = 'I love Python'):

	print('You ordered a T-shirt, size of ' + size +
		', with the words "' + words + '" on it.\n') 
	
make_shirt('L')
make_shirt('M')
make_shirt('XL', 'Fuck the M$')


def get_formatted_name(first_name, last_name):
	"""return a tidy name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
	
	l_name = input("Last name: ")
	if l_name == 'q':
		break
		
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

def build_person(first_name, last_name, age = ''):
	"""Return a dict, which include the info of a person"""
	person = {'first' : first_name, 'last' : last_name,}
	if age:
		person['age'] = age
	return person
	
musician = build_person('jimi', 'hendrix', age = 24)
print(musician)
'''

def make_album(artist, album_name, songs ='' ): ##default optional arg as NULL
	"""make a dict for an album to store the info"""
	album = {'Artist' : artist.title(), 'Album' : album_name.title() }
	if songs:    ##Add the if here!
		album['songs'] = songs
	return album
	
album1 = make_album('jay chou', 'fantasy')
album2 = make_album('bon jovi', 'crush')
album3 = make_album('metallica', 'reload', 13)

print(album1)
print(album2)
print(album3)

while True:
	print("\nThink of an album.")
	print("(Enter 'q' at any time to quit.)")
	album_name = input("Please input the name of the album. ")	
	if album_name == 'q':
		break
	artist = input("Please input the artist. ")
	if artist == 'q':
		break
	songs =  input("Please input how many songs the album has. ")
	if songs == 'q':
		break
	album = make_album(artist, album_name, songs)
	print(album)

		
