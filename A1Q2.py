"""
Name: Xiaolin Li (Josie)
Username: xli556
ID number: 455398598
Description: This program is used to encrypt a word using a Caesar cipher.
"""

message = "Caesar Cipher Encryption"
extras = 1
star_line = (len(message) + extras * 2) * "*"
print(star_line)
print("*" + message + "*")
print(star_line)
print()

name = input("Please enter a 5 letter word: ")
name = name.lower() #Make sure all the letters are lower case so that they can be found in the "alphabet"
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 5

a = alphabet.find(name[0])
a_shift = alphabet[(a + shift) % 26]
b = alphabet.find(name[1])
b_shift = alphabet[(b + shift) % 26]
c = alphabet.find(name[2])
c_shift = alphabet[(c + shift) % 26]
d = alphabet.find(name[3])
d_shift = alphabet[(d + shift) % 26]
e = alphabet.find(name[4])
e_shift = alphabet[(e + shift) % 26]

print("Encrypted word: " + a_shift + b_shift + c_shift + d_shift + e_shift)
