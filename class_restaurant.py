#!/usr/bin/env python
# -*- coding: GBK -*-
#
#dog.py
'''
class Dog():
    """a simple simulation of a dog"""
    
    def __init__(self, name, age):
        """initializing attribute name and age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
        
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
your_dog.roll_over()
'''

###homework
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):#remember the SELF in the brackets!!!
        print("This is " + self.restaurant_name.title() +", we provide " +
        self.cuisine_type.title() + " food.")
        
    def open_restaurant(self):#remember the SELF in the brackets!!!
        print(self.restaurant_name.title() + " is opening.")
    
    def set_number_served(self, number):#remember the SELF in the brackets!!!
        if number >= 0:
            self.number_served = number
        else:
            print("Customer number must be positive!")
            
    def increment_number_served(self,increment):
        #remember the SELF in the brackets!!!
        if increment > 0:
            self.number_served += increment
            
if __name__ == '__main__':        
    sichuan_food = Restaurant('chuan yu ren jia', 'sichuan')
    kurahashiya = Restaurant('kurahashiya', 'japanese')
    xiangyue = Restaurant('xiang yue', 'canton')
    
    print(sichuan_food.restaurant_name.title() + " is a restaurant's name.")
    print("It's a " + sichuan_food.cuisine_type.title() + " restaurant.")
    
    print()
    sichuan_food.describe_restaurant()
    sichuan_food.open_restaurant()
    
    print()
    kurahashiya.describe_restaurant()
    kurahashiya.open_restaurant()
    
    print()
    xiangyue.describe_restaurant()
    xiangyue.open_restaurant()
    print("\n"+str(xiangyue.number_served) +" people eating in " + 
    xiangyue.restaurant_name.title() + ".")
    #1.chang directly
    xiangyue.number_served = 50
    print("\n"+str(xiangyue.number_served) +" people eating in " + 
    xiangyue.restaurant_name.title() + ".")
    
    #2.using method
    xiangyue.set_number_served(100)
    print("\n"+str(xiangyue.number_served) +" people eating in " + 
    xiangyue.restaurant_name.title() + ".")
    
    #3.using method to increase
    xiangyue.increment_number_served(20)
    print("\n"+str(xiangyue.number_served) +" people eating in " + 
    xiangyue.restaurant_name.title() + ".")

