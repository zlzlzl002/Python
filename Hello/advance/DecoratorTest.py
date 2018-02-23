#-*- coding:utf-8 -*-
'''
Created on 2018. 2. 21.

@author: acorn
'''
import datetime
def detetime_decorator(func):
    def decorated():
        print datetime.datetime.now()
        func()
        print datetime.datetime.now()
    return decorated()

@detetime_decorator
def main_function_1():
    print "MAIN FUNCTION 1 START"
