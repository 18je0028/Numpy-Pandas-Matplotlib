# This was one of the best course in python
# course = "Programming With Mosh"
# print(course[:])
# print(course[3:7])
# print(course.upper())
# print(course.lower())
# print(course)

# firstIndexOfInputString = course.find('With')
# print(firstIndexOfInputString)

# newCourse = course.replace('Mosh','Harry')
# print(newCourse)

# import math
# print(math.ceil(4.678)) # o/p-- 5
# print(math.floor(4.999902)) # o/p-- 4
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# print(matrix[0])

# # 1st way

# for i in range(0,3):
#     for j in range(0,3):
#         print(matrix[i][j],end=" ")
#     print("")


# print("")
# # 2nd way

# for row in matrix:
#     for item in row:
#         print(item,end=" ")
#     print("")

# def AboutYourself():    
#     print("Walmart is the best company")
#     print("Abhishek is going to join walmart as an intern in summer of 2022")
#     print("He is ready to learn new concepts and is really exvited about it.")

# import Chapter12.Chapter12_1
# Chapter12.Chapter12_1.Greet("kong")

# ------

# from Chapter12.Chapter12_1 import Greet

# Greet("monster")
# Greet("abhishek")
# Greet("walmart")


# -------

# from Chapter12 import Chapter12_1

# Chapter12_1.Greet("kongikon")
# mx = Chapter12_1.findMax([34,56,12,34,25,56,78,0,23,45])
# print(mx)

# -----------

# Rnadom Module in python

import random

# prints real numbers b/w [0,1)
# for i in range(0,3):
#     a = random.random()
#     print(a)

# If we want numbers b/w [10,20]
# for i in range(0,3):
#     a = random.randint(10,20)
#     print(a)

# If we want to choose a random leader from a group
# members = ["Abhishek","Vishal","Shivam","Villy","Archit"]
# leader = random.choice(members)
# print(f"The leader of the group is {leader}")

# -----------------------------------------------------------------------

# Working with directories in python

# pathlib is a module and Path is a class is defined under it

# from pathlib import Path

#Absolute path -> hard disk se pura path ko define karna
# c:\Program\Microsoft
#Relative path -> Jaha p aabhi hai waha se path define karna
# ----------
# path = Path("Chapter12")
# print(path.exists()) # checks whether this directory(here "Chapter12") is present in our relative place or not
# ------------
# To create a new dirctory we use mkdir(meaning make directory) function
# path = Path("Emails")
# path.mkdir()
# To remove directory we use rmdir function
# path.rmdir()
# ---------------------
# path = Path("C:\\Users\\Abhishek\\ProgrammingWithHarryInPython")
# print(path.exists())
# To print all the files inside ProgrammingWith Harry
# for file in path.glob("*"):
#     print(file)
# To print all the files inside ProgrammingWithHarry with extension .py
# for file in path.glob('*.py'):
#     print(file)

# ---------------------------------------------------------------------------------------------------------









