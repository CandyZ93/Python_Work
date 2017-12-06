'''
unconfirmed_users =['alice', 'brain', 'candace',]
confirmed_users = []

#check every user, until no user is left
#move users to confirmed list
while unconfirmed_users:
    current_user =  unconfirmed_users.pop()

    print("Veryfying user: " + current_user.title())
    confirmed_users.append(current_user)

#print confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', ]
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

#set a label, point out continue or not
polling_active = True

while polling_active:
    #remind to input interviewee's name and response
    name = input("\nWhat is your name? ")
    response = input("Which moutain you'd like to climb? ")

    #save the answer in the dict
    responses[name] = response

    #check is there anyone want to answer the question
    repeat = input("Would you like to let another person \
respond? (yes/no) ")
    if repeat == 'no':  ###avoid to process or print label 
        polling_active = False

    #close the polling and print the result
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name.title() + " would like to climb " + response.title() + ".")
'''
##--home work
sandwich_orders = ['beef', 'pastrmi', 'tuna', 'pastrmi', 'eggroll','pastrmi',]
finished_sandwiches = []
print("Sorry, We have run out pastrmi!")
while 'pastrmi' in sandwich_orders:
    sandwich_orders.remove('pastrmi')
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThese sandwiches are finished:")
for sandwich in finished_sandwiches:
    print("\t" +sandwich +" sandwich.")
                

