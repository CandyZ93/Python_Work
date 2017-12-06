#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_user_log.py

class User():
    def __init__(self, first_name, last_name, u_id, level ):
        self.first_name = first_name
        self.last_name = last_name
        self.u_id = u_id
        self.level = level
        self.login_attempts = 0
        
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("\nThis is " + full_name.title() + ":")
        print("- ID: " + str(self.u_id))
        print("- Level: " + str(self.level))
        
    def greet_user(self):
        print("Welcome back, " + self.first_name.title() + ' ' +
        self.last_name.title() + "!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def get_full_name(self):
        fname = self.first_name.title() + ' ' + self.last_name.title()
        return fname
        
if __name__ == '__main__':
    user1 = User('lance', 'zhou', 741002686, 100)
    user2 = User('tom', 'hanks', 9555555, 100)
    user3 = User('jet', 'lee', 1234567, 99)
    
    user1.describe_user()
    user1.greet_user()
    
    user2.describe_user()
    user2.greet_user()
    
    user3.describe_user()
    user3.greet_user()
    
    print(user3.get_full_name() + " has logged " +
    str(user3.login_attempts) + " times.")
    for i in range(50):
        user3.increment_login_attempts()
    print("\n"+user3.get_full_name() + " has logged " +
    str(user3.login_attempts) + " times.")
    user3.reset_login_attempts()
    print("\n"+user3.get_full_name() + " has logged " +
    str(user3.login_attempts) + " times.")
    
