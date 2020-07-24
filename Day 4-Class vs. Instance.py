# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:07:22 2020

@author: ankit.khule
"""

class Person:
    age=0
    def __init__(self,initialAge):
        self.initialAge=initialAge
        if self.initialAge < 0:
            self.initialAge=0
            print('Age is not valid, setting age to 0.')
        else:
            Person.age=self.initialAge
            
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if Person.age < 13:
            print('You are young.')
        elif Person.age>=13 and Person.age<18:
            print('You are a teenager.')
        elif Person.age>=18:
            print('You are old.')
        
    def yearPasses(self):
        if Person.age<18:
            # Increment the age of the person in here
            Person.age+=1
        
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")