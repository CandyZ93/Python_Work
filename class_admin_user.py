#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_admin_user.py

from class_user_log import User

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post",
    "can ban user", "can clear the screen"]
    
    def show_privileges(self):
        print("The admin has such privileges:")
        for privilege in self.privileges:
            print("- " + privilege)
    
class Admin(User):
    def __init__(self, first_name, last_name, u_id, level):
        super().__init__(first_name, last_name, u_id, level)
        self.privileges = Privileges()
        #self.privileges = ["can add post", "can delete post", 
       # "can ban user"]
        
    '''def show_privileges(self):
        print("The admin has such privileges:")
        for privilege in self.privileges:
            print("- " + privilege)
    '''
                
if __name__ == '__main__':
    '''admin1 = Admin('John', 'Woo', 10001, 1000)
    admin1.show_privileges()
    
    admin1.describe_user()
    admin1.greet_user()
    '''
    
    admin2 = Admin('John', 'Woo', 10001, 1000)
    admin2.privilegs = ["can add post", "can delete post",
    "can ban user", "can clear the screen"]
    
    admin2.describe_user()
    admin2.greet_user()
    
    print()
    
    admin2.privileges.show_privileges()
