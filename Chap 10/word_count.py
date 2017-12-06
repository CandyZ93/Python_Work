#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  word_count.py



def count_words(file_name):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_name, encoding = 'UTF-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        '''msg = "Sorry, the file " + file_name + " does not exist."
        print(msg)'''
        pass
        
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + 
        " words.")

if __name__ == '__main__':
    #file_name = 'alice.txt'
    filenames = ['alice.txt', 'Beethoven.txt', 'How_to_Sing.txt', 
    'siddhart.txt', 'Musical_Memories.txt']
    for file_name in filenames:
        count_words(file_name)
