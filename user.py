users = ['Lance', 'John', 'jack', 'riTa', 'admin', 'lucY']
userLogin=input("Type in your name:")

if userLogin in users:
	if userLogin == 'admin':
		print("Hello admin, wanna see status report?")
	else:
		print("Hello "+userLogin+"! Welcome home!")
else:
	choice=input("No such user! Need registration?\[Y/n\]\n")
