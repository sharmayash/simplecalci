# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 11:52:14 2017

@author: yash
"""
""" yash sharma """
while True:
    print("options:")
    print("enter 'add' for addition of two numbers ")
    print("enter 'sub' for subtraction of two numbers ")
    print("enter 'mul' for multiplication of two numbers ")
    print("enter 'div' for division of two numbers ")
    print("enter 'quit' to end the program ")
    user_input = input(": ")
    
    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("enter a number : "))
        num2 = float(input("enter another number : "))
        result = str(num1 + num2)
        print("the answer is " + result)
    
    elif user_input == "sub":
        num1 = float(input("enter a number : "))
        num2 = float(input("enter another number : "))
        result = str(num1 - num2)
        print("the answer is " + result)
    
    elif user_input == "mul":
        num1 = float(input("enter a number : "))
        num2 = float(input("enter another number : "))
        result = str(num1 * num2)
        print("the answer is " + result)
    
    elif user_input == "div":
        num1 = float(input("enter a number : "))
        num2 = float(input("enter another number : "))
        result = str(num1 / num2)
        print("the answer is " + result)
        
    else:
        print("unknown input")