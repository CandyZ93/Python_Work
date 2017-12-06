#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  survey.py

class AnonymousSurvey():
        """收集匿名调查问卷的答案"""
        
        def __init__(self, question):
            """存储一个问题， 并为存储答案做准备"""
            self.question = question
            self.responses = []
            
        def show_question(self):
            """显示调查问卷"""
            print(self.question)
        
        def store_response(self, new_response):
            """存储单份调查答卷"""
            self.responses.append(new_response)
            
        def show_results(self):
            """显示收集到的所有答卷"""
            print("Survey results:")
            for response in self.responses: #don't forget self.
                print('- ' + response.title())
                
    
if __name__ == '__main__':
    question = "Who the fuck are you?"
    survey1 = AnonymousSurvey(question)
    survey1.show_question()
