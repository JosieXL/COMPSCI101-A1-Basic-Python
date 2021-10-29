"""
Name: Xiaolin Li (Josie)
Username: xli556
ID number: 455398598
Description: This program is used to prompt a user to enter their name, and using that name, generate them a University of Auckland username.
"""
import random

message = "University of Auckland Username Generator"
extras = 2
star_line = (len(message) + extras * 2) * "*"
blanks = extras * " "
print(star_line)
print(blanks + message)
print(star_line)
print()

name = input("Please enter your name: ")
name = name.lower() #Make sure all the letters are in lowercase
space = name.find(" ")
first_name = name[:space]
last_name = name[space + 1:]
username_letters = first_name[0] + last_name[0:3]
number = random.randrange(1,999)

username_numbers = "00" + str(number)#This need to be a string to be printed out
username_numbers = username_numbers[-3:] #Make sure there are 3 digit numbers
print()
print("Your username is " + username_letters + username_numbers)
