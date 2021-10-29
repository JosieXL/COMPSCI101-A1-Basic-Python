"""
Name: Xiaolin Li (Josie)
Username: xli556
ID number: 455398598
Description: This program is used to calculate the surface area and volume of a right circular cone.
"""
import math

message1 = "Right Circular Cone"
message2 = "Surface Area and Volume Calculator"
extras = 7
sign_line = len(message2) * "#" #line of "#"
blanks = extras * " "

print(sign_line)
print(blanks + message1)
print(message2)
print(sign_line)
print()

radius = int(input("Radius: "))
height = int(input("Height: "))
print()

surface_area = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
surface_area = round(surface_area, 4) #Make sure the value rounded to 4 decimal points
volume = 1 / 3 * math.pi * radius ** 2 * height
volume = round(volume, 4)

print("Surface Area: ", surface_area, sep= "")
print("Volume: ", volume, sep = "")

