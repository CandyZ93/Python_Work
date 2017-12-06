users = ['Lance', 'John', 'jack', 'riTa', 'admin', 'lucY']

def choiceAdd():
	Flag_C = True
	while(Flag_C):		
		choice=input("No such user! Need registration?[Y/n]\n")
		if choice in ['Y' ,'y' ,'yes','Yes']:
			Flag_C = False
			print("Good choice, we are happy to have a new friend!")
			userAdd()						
		elif choice in ['N', 'n', 'no', 'No']:
			print("Goodbye! Happy everyday!")
			exit(1)
		else:
			print("Sorry! Illegal input!\n")

def userAdd():
	Flag_ua = True
	while(Flag_ua):
		newuser=input("Now think a cool name:")
		lower_users = [] 
		for user in users:
			lower_users.append(user.lower())
		if newuser.lower() in lower_users:
			print("Name already used!")
		else:
			users.append(newuser)
			Flag_ua = False
			print("Successfully Registed! Welcome, "+newuser+"!")
			print(users)			
		
if users:
    userLogin=input("Type in your name:")
    if userLogin in users:
	    if userLogin == 'admin':
		    print("Hello admin, wanna see status report?")
	    else:
		    print("Hello "+userLogin+"! Welcome home!")
    else:
	    choiceAdd()
else:
    print("Damn we don't have any user! We are fucked up!")
	
