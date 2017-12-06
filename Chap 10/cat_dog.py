#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cat_dog.py


def petname(filename):
    """print the name of the pets in file."""
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        """print("Can not find " + filename + ".")"""
        pass
    else:
        print(filename.split(".")[0].title()+ " has these names:")
        for line in lines:
            print("\t" + line.rstrip())
    
    

if __name__ == '__main__':
    filenames = ['cats.txt', 'dogs.txt']
    for filename in filenames:
        petname(filename)
