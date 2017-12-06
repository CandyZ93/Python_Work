   #!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_import.py

from class_restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'grape', 'chocolate']
        
    def show_flavor(self):
        print("We have these kind of flavors:")
        for flavor in self.flavors:#SELF.flavors!
            print("- " + flavor.title())
            
iceking = IceCreamStand('ice king', 'icecream&drinks')
iceking.show_flavor()
iceking.open_restaurant()
iceking.describe_restaurant()

