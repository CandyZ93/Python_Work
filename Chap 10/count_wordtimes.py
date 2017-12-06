#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  count_wordtimes.py



def count_wordtimes(filename, word = 'the'):
    try:
        with open(filename, encoding = "UTF-8") as f_obj:
            num = f_obj.read().lower().count(word)#f_obj can not use lower method
            #f_obj.read() can
    except FileNotFoundError:
        print(filename + " not found!")
    else:
        print(filename + " has " +str(num) +" '" + word +"'.")
        
    

if __name__ == '__main__':
    '''filenames = ['cats.txt', 'dogs.txt']
    for filename in filenames:
        count_wordtimes(filename, 'tom')'''
    filenames = ['alice.txt', 'Beethoven.txt', 'How_to_Sing.txt', 
    'Musical_Memories.txt']
    for filename in filenames:
        count_wordtimes(filename)
