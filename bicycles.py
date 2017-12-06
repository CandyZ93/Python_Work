bicycles = ['trek', 'cannondale', 'redline', 'specialized']

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
motorcycles.insert(0,'CFmoto')
message = "My first bike was a " + motorcycles[2].title() + " Jog-i.\n"
print(motorcycles)
print(message)

del motorcycles[0]
print("deled:")
print(motorcycles)

motorcycles.insert(0,'CFmoto')
dreamBike = motorcycles.pop()
print("My dream bike is "+dreamBike.title()+" .\n")

cheapBike=motorcycles.pop(0)
print("Mostly possible to own a " + cheapBike +" because it's cheap.\n")
print(motorcycles)

bestSeller = "honda"
motorcycles.remove(bestSeller)
print(bestSeller.title()+" is the biggest bike manufacturer on earth.")
print(motorcycles)
