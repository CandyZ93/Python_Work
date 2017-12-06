#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alice_FNFError.py

if __name__ == '__main__':
    file_name = 'alice.txt'
    try:
        with open(file_name, encoding = 'UTF-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " does not exist."
        print(msg)
        
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + 
        " words.")
