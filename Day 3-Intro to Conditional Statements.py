# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:03:31 2020

@author: ankit.khule
"""

def wierrd(N):
    if (N>=2 and N<6) or (N>20):
        print('Not Weird')
    elif (N>=6 and N<21) :
        print('Weird')

if __name__ == '__main__':
    N = int(input())
    if ((N%2)!=0):
        print('Weird')
    if ((N%2)==0):
        wierrd(N)