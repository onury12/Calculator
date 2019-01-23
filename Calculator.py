#! /usr/bin/env python
# -*- coding: UTF-8 -*-
print("Calculator")
print("==========")
def screen():
 print("To Addition 1")
 print("To Subtraction 2")
 print("To Multiply 3")
 print("To Divide 4")
def calculation():
 choice = input("Please Chose Your Operation:")
 number1 = int(input("Please Enter First Number:"))
 number2 = int(input("Please Enter Second Number:"))
 if choice == "1":
  print(number1, "+", number2, "=", (number1+number2))
 elif choice == "2":
  print(number1, "-", number2, "=", (number1-number2))
 elif choice == "3":
  print(number1, "x", number2, "=", (number1*number2))
 elif choice == "4":
  print(number1, ":", number2, "=", (number1/number2))
 else:
  print("Error")
def select():
 selection = input("To Restart Press 5, To Escape Press 6:")
 if selection == "5":
  screen()
  calculation()
  select()
 if selection == "6":
  pass
screen()
calculation()
select()


