# str = "Abhishek will be joining Walmart in the month of may, nextyear. He is upset because he didn't joined Amazon , but he will be doing well in Walmart"
# print("length of str is : " , len(str))
# print("number of occurences of letter 'a' in the string str is : " , str.count("a"))
# print("number of occurences of string 'Walmart' is : " , str.count("Walmart"))
# print("is string 'Abhishek' present in the string str : " , str.find("Abhishek"))
# print("is string 'Walmart' present in the string str : " , str.find("Walmart"))

# JoiningLetter = '''Dear |NAME| ,
# I am your HR from the company WalmartGlobalTechIndia , I am happy to announce that you are selected as a summer intern for the next summer. 
# We at WalmartGlobalTechIndia is happy to receive you , congrats. You will be joining on : |DATE|'''

# JoiningLetter = JoiningLetter.replace("|NAME|","Abhishek")
# JoiningLetter = JoiningLetter.replace("|DATE|","05/05/2022")
# print(JoiningLetter)

# str = "Walmart is happy to take you in  , Abhishek"
# print(str)
# str = str.replace("  "," ")
# print(str)

#----------------------------------------------------------------------------------------------------------------------------------------------

# Lists and Tuples

# arr = [1,2,-45,45,4]
# print(type(arr))
# print(arr[-1])

# favouriteWords = ["Abhishek" , "Walmart" ,"IIT" , 2018 , "NIT" ,  9119215817 , "RCB" ,"HardWork" , "abhi821005" , 1212 , 8210058406 ]

# print(favouriteWords[0])
# print(favouriteWords[0:4])
# print(type(favouriteWords))
# print(type(favouriteWords[1]))
# print(type(favouriteWords[-1]))

# -----------------------------------------------------------------------------------------------------------------------------------------------


# Dictionary in python

# myDict = {
#     "Walmart" : "Fortune 1 company" ,
#     "Abhishek" : "A student",
#     "arr" : [2312 , 2018 , 1998 , 1212] ,
#     2022 : "The year of joining Walmart as an intern" ,
#     "anotherDict" : {
#         "Google" : "Dream Company",
#         "Requirement" : "Talent and Problem Solving"
#     }
# }

# print(type(myDict))
# print(myDict["Walmart"])
# print(myDict["anotherDict"])
# print(myDict["anotherDict"]["Requirement"])
# print(myDict["arr"])
# print(myDict[2022])

# myDict["arr"].append(821005)
# print(myDict["arr"])
# myDict["arr"].sort()
# print(myDict["arr"])

# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())

# Update Dictionary

# updDict = {
#     "friend" : ["shivam" , "vishal"] ,
#     "college" : "IIT ISM DHANBAD" ,
#     "Branch" : "Mathematics and Computing"
# }

# myDict.update(updDict)
# print(myDict)

# ------------------------------------------------------------------------------------------------------------------------------------------


# Sets in python

# a = set()
# a.add(45)
# a.add(45)
# a.add(2)
# a.add(4)
# a.add((32,21,78,-45,-21,-32)) # can add a tuple which is not hashable
# print(type(a))
# print(a)

# A nother way to declare sets
# b = {2,6,3,4,8,7,1}
# b.add(18)
# b.add("18")
# print(b)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Conditional operator in python

# a = int(input())

# if(a>100) :
#     print("The number is greater than 100")
# elif(a>50):
#     print("The number is lesser than 100 but greater than 50")
# else :
#     print("the number is lesser or eaual than 50")

# a = None
# if(a==None):
#    print("yes")
# else:
#    print("NO")

# arr = [45,23,1,567,35]

# if(57 in arr):
#   print("yes")
# else:
#   print("no")


# --------------------------------------------------------------------------------------------------------------------------------------------------

# Loops in python

# Companies = ["Walmart" , "Google" , "Sprinklr" , "Oracle" , "Microsoft" , "Amazon" , "Myntra" , "Goldman Sachs" , "Arista" , "Publicis Sapient" , "Nutanix" , "Newzera" , "Instabase"]
# Companies.append("Salesforce")
# Companies.append("Linkedln")
# Companies.append("Tata steel")
# Companies.append("Udaan")
# Companies.append("Codenation")
# Companies.append("Dynamic technology")
# Companies.append("Uber")
# Companies.append("Flipkart")
# Companies.append("Morgan Stanley")
# Companies.append("DisneyHotstar")
# Companies.append("Nvidia")
# Companies.append("Razorpay")

# id = 0
# length = len(Companies)

# # Using while loop in python
# while(id<length):
#     print(Companies[id])
#     id+=1

# # Using for loop in python
# for company in Companies:
#   print(company)

# Range fuction in python

# for i in range(8):
#    print(i)

# print('\n')


# for i in range(1,8):
#   print(i)

# print('\n')

# for i in range(1,8,2):
#   print(i)

# print('\n')

# for i in range(2,8,3):
#   print(i)

# Pass in python


# def sumFunction(a,b) :
#   pass

# i = 4

# if i > 4 :
#   pass
#   while(i<10) :
#     print(i)
#     i+=1
# else :
#   print("monster")

# ----------------------------------------------------------------------------------------------------------------------------------------------


# while 1 :
#   n = int(input())
#   i = 2
#   while i*i<=n :
#     if n%i==0 :
#       print("not prime")
#       break;
#     i+=1
#   else:
#       print("prime")


# n = int(input("Enter the number : "))

# for i in range(1,n+1) :
#  if i == 1 or i == n :
#    print("*"*n)
#  else :
#    print("*",end="")
#    print(" "*(n-2),end="")
#    print("*")

# Enter the number : 10
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

# n = int(input())

# for i in range(1,n+1) :
#    print(" "*(n-i),end="")
#    print("*"*(2*i-1),end="")
#    print(" "*(n-i))


#    10
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************


# ------------------------------------------------------------------------------------------------------------------------------------------------


# Functions in python

# def Greetings(name="Stranger"):
#   print("Good morning, " + name)

# def PercentageCalculation(marks):
#    return sum(marks)/len(marks)


# Greetings("Abhishek")
# Greetings()
# print(PercentageCalculation([34,89,55,100]))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Recursion in python

# def Fact_iteration(n):
#   product = 1
#   for i in range(1,n+1):
#    product *= i

#   return product

# def Fact_recursion(n):
#   if n==0:
#     return 1
#   return n*Fact_recursion(n-1)


# print(Fact_recursion(4))
# print(Fact_iteration(5))


# def RemoveWordFromString(str,word):
#     newstr = str.replace(word,"")
#     return newstr.strip()

# str = "   this is abhishek, and he is working at walmart       "

# print(str.strip())
# print(str)
# print(RemoveWordFromString(str,"abhishek"))


# ---------------------------------------------------------------------------------------------------------------------------------------------

# File I/O in python

# Reading in a file
# file = open('sample.txt','r')
# data = file.read()
# print(data)
# file.close()

# Writing in a file

# file = open("anpther.txt",'w')
# file.write("Glorious")
# file.close()

# With statement use in python , here we don't need to write file.close()

# with open("sample.txt",'w') as f :
#     a = f.write(".I am a monster")
#     print(a)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# def game():
#     score = int(input("Enter the game score: "))
#     return score


# while 1:
#     score = game()
#     with open("sample.txt") as file:
#         hi_score = int(file.read())
#     if score > hi_score:
#        with open("sample.txt",'w') as file:
#           file.write(str(score))


# MUltiplication table from 2 to 20 for children in the file Table

# for start in range(2,21):
#    st = "Tables/multiplication table of " + str(start) + ".txt"
#    with open(st,'w') as file:
#       for i in range(1,11):
#         content = str(start)+" * "+str(i)+" = "+str(start*i)
#         file.write(content)
#         file.write('\n')

# with open("sample.txt") as file:
#    str = file.read()

# newstr = str.replace("donkey","#####")

# with open("sample.txt",'w') as file:
#    file.write(newstr)

# -------------------------------------------------------------------------------------------------------------------

# OOPS in python

# class RailwayForm:
#     formType = "RailwayForm"
#     def printData(self):
#         print(f"Name of the traveller is : {self.name}")
#         print(f"Train from which the traveller will travel is : {self.trainNo}")
#         print(f"Traveller will start his journey from : {self.src}")
#         print(f"Traveller will travel upto : {self.dest}")

# AbhiTheTraveller = RailwayForm()
# AbhiTheTraveller.name = "Abhishek kumar"
# AbhiTheTraveller.trainNo = "patna-hatia"
# AbhiTheTraveller.src = "delhi"
# AbhiTheTraveller.dest = "gaya"
# AbhiTheTraveller.printData()

# class Employee:
#     company = "Google"

# Abhishek = Employee()
# Shivam = Employee()

# Abhishek.salary = 32.5

# print(Abhishek.salary)
# # print(Shivam.salary)



# class Employee:
#     company = "Google"
#     salary = 23
#     def printData(self):
#         print(self.salary)

# Abhishek = Employee()
# Abhishek.salary = 24.5
# Abhishek.printData()

# --------

# Static method in class

# class Employee:
#     company = "Google"
#     salary = 23
#     def printData(self):
#         print(self.salary)
#     @staticmethod
#     def greet():
#         print("Good Morning, sir")
#     def luciferMorningstar(self,signature):
#         print(f"he is the devil and is on earth when thrown from heaven \n{signature}")

# Abhishek = Employee()
# Abhishek.salary = 24.5
# Abhishek.printData() # Employee.printData(Abhishek)
# Abhishek.greet()   #Employee.greet()
# Abhishek.luciferMorningstar("Thanks!")

# ---

#  Constructor in python


# class Employee:
#     company = "Google"
#     salary = 23

#     def __init__(self,name,salary,company):
#         print("Constructor is called")
#         self.name = name
#         self.salary = salary
#         self.company = company
    
    
#     def printData(self):
#         print(self.name)
#         print(self.salary)
#         print(self.company)

#     @staticmethod
#     def greet():
#         print("Good Morning, sir")
#     def luciferMorningstar(self,signature):
#         print(f"he is the devil and is on earth when thrown from heaven \n{signature}")

# Abhishek = Employee("Abhishek",25,"Walamrt")
# Abhishek.printData()

# -----------------------------------------------------------------------------------------------------------------------------------

# class Calculator:
#     def __init__(self,number):
#         self.number = number
#     def square(self):
#         print(f"The square of the number {self.number} is {self.number**2}")
#     def squareRoot(self):
#         print(f"The squareRoot of the number {self.number} is {self.number**0.5}")
#     def cube(self):
#         print(f"The cube of the number {self.number} is {self.number**3}")

# n = Calculator(9)
# n.square()
# n.squareRoot()
# n.cube()


#-------------------

# class IndianRailways:
#     trains = []
#     def __init__(self,trains) -> None:
#          self.trains = trains
#     def seatsAvailable(self,trainName):
#         for trainDetails in self.trains:
#             if trainDetails[0]==trainName:
#                 return trainDetails[2]
#     def priceOfTicket(self,trainName):
#         for trainDetails in self.trains:
#             if trainDetails[0]==trainName:
#                 return trainDetails[1]
#     def bookATicket(self,trainName):
#         for trainDetails in self.trains:
#             if trainDetails[0]==trainName and trainDetails[2]>0:
#                 trainDetails[2]-=1
#                 return True
#         return False


# Abhishek = IndianRailways([["Rajdhani",2345,50],["Satabdi",2569,20]])
# print(Abhishek.seatsAvailable("Rajdhani"))
# print(Abhishek.seatsAvailable("Satabdi"))
# Abhishek.bookATicket("Rajdhani")
# Abhishek.bookATicket("Satabdi")
# print(Abhishek.seatsAvailable("Rajdhani"))
# print(Abhishek.seatsAvailable("Satabdi"))

#--------------------------------------------------------------------------------------------------------------------------------------------

# Intheritance in python

# class Employee:
#     company = "Walmart"
    
#     def aboutEmployee(self):
#         print(f"The employee is in {self.company} company ans his name is {self.name}")

# class Programmer(Employee):
#     language = "python"

#     def aboutProgrammer(self):
#         print(f"The employee is in {self.company} company ans his name is {self.name}. His preffered language is {self.language}")



# e = Programmer()
# e.name = "Abhishek"
# e.aboutProgrammer()

# E = Employee()
# E.name = "Monster"
# E.aboutEmployee()


#-----------------------------------

# class Employee:
#     company = "Walmart"
    
#     def aboutEmployee(self):
#         print(f"The employee is in {self.company} company ans his name is {self.name}")

# class Freelancer:
#     company = "Networking"
#     uplevel = 0

#     def upgradeLevel(self):
#         self.uplevel+=1

# class Programmer(Employee,Freelancer):
#     language = "python"

#     def aboutProgrammer(self):
#         print(f"The employee is in {self.company} company ans his name is {self.name}. His preffered language is {self.language}")


# p = Programmer()
# print(p.company) # walmart will be printed because it is written first after declaring class Programmer

# Super method in python

# class Person:
#     country = "India"

#     def __init__(self) -> None:
#         print("I am in Person constructor\n")

#     def takeBreath(self):
#         print("Breath India")

# class Employee(Person):
#     company = "Walmart"

#     def __init__(self) -> None:
#         super().__init__()
#         print("I am in Employee constructor\n")
    
#     def aboutEmployee(self):
#         print(f"The employee is in {self.company} company ans his name is {self.name}")
    
#     def takeBreath(self):
#         super().takeBreath()
#         print("Breath Employee")

    

# class Programmer(Employee):
#     language = "python"

#     def __init__(self) -> None:
#         # super().__init__()
#         print("I am in programmer constructor")

#     def aboutProgrammer(self):
#         print(f"The employee is in {self.company} company ans his name is {self.name}. His preffered language is {self.language}")
    
#     def takeBreath(self):
#         super().takeBreath()
#         print("Breath Programmer")


# p = Programmer()
# p.takeBreath()

#---------------------------------

# Class methods in python

# class Employee:
#     name = ""
#     company = "Walmart"
#     salary = 25

#     def __init__(self,name,company,salary) -> None:
#         self.name = name
#         self.company = company
#         self.salary = salary

#     # def changeSalary(self,sal):
#     #     # self.salary = sal  # only changes the self.salary not the class salary
#     #     self.__class__.salary = sal # this changes the class salary to sal not self.salary to sal, it only changes the class attribute
    
#     @classmethod
#     def changeSalary(cls,sal):
#         cls.salary = sal # this changes the class attribyte salary


# e = Employee("Abhishek","Walmart",22)

# print(e.salary)
# e.changeSalary(27)
# print(e.salary)
# print(Employee.salary)

# -------------------------------------------

# (Property decorator or  getter) , setter in python

# class Employee:
#     company = "Walmart"
#     salary = 115000
#     salaryBonus = 30000
#     # totalSalary = salary + salaryBonus # but this keeps on changing because salaryBonus changes everytime

#     @property
#     def totalSalary(self):
#         return self.salary + self.salaryBonus
    
#     @totalSalary.setter
#     def totalSalary(self,newToatalSalary):
#         self.salaryBonus = newToatalSalary - self.salary
    
#     def printDetails(self):
#         print(f"The total salary of employee is {self.totalSalary} \n Where salary = {self.salary} \n salaryBonus = {self.salaryBonus} ")
    

# e = Employee()
# e.printDetails()

# # totalSalary is not any attribute of class Employee , it just depends on some attribytes of class Employee which keeps on changing
# e.totalSalary = 150000
# e.printDetails()

# -------------------------------------

# operator overloading in python



# class Complex:
#     real = 0
#     img = 0

#     def __init__(self,real,img):
#         self.real = real 
#         self.img = img 
    
#     def __add__(self,c):
#         print(f"Let's add 2 complex numbers")
#         comp = Complex(self.real+c.real , self.img+c.img)
#         return comp
    

# c1 = Complex(3,5)
# c2 = Complex(4,2)

# # both are same
# # c3 = c1.__add__(c2) 
# c3 = c1 + c2

# print(f"ans = {c3.real} + {c3.img}i")


#----------------------------------------------------------------------------------------------------------------------------------------------------\

# class C2dVector:
#     def __init__(self,i,j) -> None:
#         self.icap = i
#         self.jcap = j
    
#     def printDetails(self):
#         print(f"{self.icap}i+ {self.jcap}j+ ",end="")
    
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVector(C2dVector):
#     def __init__(self, i, j,k) -> None:
#         super().__init__(i, j)
#         self.kcap = k

#     def printDetails(self):
#         super().printDetails()
#         print(f"{self.kcap}k")

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


# v2d = C2dVector(1,5)
# v3d = C3dVector(2,5,7)

# print(v2d)
# print(v3d)

# class Vector:
#     def __init__(self,vector) -> None:
#         self.vector = vector
    
#     def __str__(self) -> str:
#         str = ""
#         for i in range(0,len(self.vector)):
#             str += f"{self.vector[i]}A{i} +"
#         return str[0:-1]
    
#     def __add__(self,newArr):
#         newList = []
#         for i in range(0,min(len(self.vector),len(newArr.vector))):
#             newList.append(self.vector[i]+newArr.vector[i])
        
#         if(len(self.vector)>len(newArr.vector)):
#             for i in range(len(newArr.vector),len(self.vector)):
#                 newList.append(self.vector[i])
#         else:
#             for i in range(len(self.vector),len(newArr.vector)):
#                 newList.append(newArr.vector[i])

#         return (Vector(newList))

#     def __mul__(self,newArr):
#         dotProduct = 0
#         for i in range(0,min(len(self.vector),len(newArr.vector))):
#             dotProduct += self.vector[i]*newArr.vector[i]
#         return dotProduct


# arr = Vector([1,2,5,3])
# print(arr)
# brr = Vector([2,1,3,2])
# print(brr)

# print(arr+brr)
# print(arr*brr)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Exception Handling in python

# while True:
#     print("Enter quit for Exit\n")
#     a = input("Enter a number: ")

#     if a == "quit":
#         break

#     try:
#         print("Trying...")
#         a = int(a)
#         print("No Error Found!")
#         if a>6 :
#             print("The number you entered is greater than 6")
#         else:
#             print("The number you entered is less than 7")
#     except Exception as e:
#         print(f"Error 404 !!! {e}")

# print("Sucessful Compilation")

# --------------------------------------

# while True:
#     try:
#         a = int(input("Enter a number whose reciprcal you wanna find: "))   
#         a = 1/a   
#         print(a) 
#     except ValueError as e:
#         print("Please enter a valid input")
#     except ZeroDivisionError as e:
#         print("Please make sure that you are not writing 0 as the number")
#     except:
#         print("Another error")

# print("Thanks for your time , Have a good day!!!")  

# ------------------

# def increment(num):
#     try:
#         return int(num)+1
#     except ValueError as e:
#         raise ValueError("You have entered a wrong value")


# print(increment("harry"))


# ----------------------------

# try:
#     a = int(input("Enter a number: "))
#     a = 1/a
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print("We got no error")

#-------------------------------------


# try:
#     a = int(input("Enter a number: "))
#     a = 1/a
#     print(a)
# except Exception as e:
#     print(e)
#     exit()
# finally:
#     print("We are done")

# ----------------------------------------------------------------

# global keyword in python

# a = 54 # global variable

# def fun1():
#     global a # 
#     print(a)
#     a=4 # local variable but when global a is written it becomes the same one outside (global one)
#     print(a)

# fun1()
# print(a)


# ---------------------------------------------------

# enumerate function in python

# list1 = [56,3.56,-54,235,"harry",True]

# # index=0
# # for item in list1:
# #     print(item,index)
# #     index+=1

# for index,item in enumerate(list1):
#     print(item,index)

# ---------------------------------------------------

# List comprehension in python

# a = [34,3,2,67,54,4041,4090,2018,1212,567,3,2]

# # b = []
# # for i in range(0,len(a)):
# #     if a[i]%2==0:
# #         b.append(a[i])


# # shortcut to write the same
# b = [i for i in a if i%2==0]
# print(b)

# b = [i for i in a if i>4000]
# print(b)

# b = {i for i in a}
# print(b)

# --------------------------

# def fileRead(filename):
#     with open(filename,'r') as f:
#         print(f.read())

# def fileIsPresentOrNot(filename):
#     try:
#         with open(filename,'r') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"File {filename} is not found")
#     except Exception as e:
#         print(f"This file is not present. {e}")


# fileIsPresentOrNot("1.txt")
# fileIsPresentOrNot("2.txt")
# fileIsPresentOrNot("3.txt")

# ------------------------------------------------------------------------


# arr = [1,2,3,4,5,6,7,8,9,10]

# for i,item in enumerate(arr):
#     if i==2 or i==4 or i==6:
#         print(item,end=" ")

# print(f"\n")

# num = int(input("Enter a number : "))

# brr = [num*i for i in range(1,11) ]
# print(brr)

# print(str(brr))

# with open("1.txt","w") as f:
#     for item in brr:
#         f.write(f"{item} ")

# --------------------------------------------------------------------------------------------------------


# '''
#    error ko hatane k liye--> Set-ExecutionPolicy Unrestricted -Scope Process
#   path hai y wala -->  .\myprojectenv\Scripts\activate.ps1

# '''

# import flask
# import pandas as pd
# import pygame



# Virtual enviornment in python

# --------------------------------------

# Lambda fuunctions in python

# def add100(x):
#     return x+100

# def square(x):
#     return x*x

# def addThreeNumbers(a,b,c):
#     return a+b+c


# add100 = lambda x : x+100
# square = lambda x : x*x
# addThreeNumbers = lambda a, b, c : a+b+c

# print(add100(25))
# print(square(5))
# print(addThreeNumbers(17,3,5))

# -------------------------------------------------------------------------------------------------------------

# Join methods in python

# listCompanies = ["Apple","Microsoft","Walmart","Amazon","Swiigy","Zomato","Oracle","Google","Facebook","Twitter","Linkldn","Jio"]
# topComapnies = ("Apple","Microsoft","Walmart","Amazon","Swiigy","Zomato","Oracle","Google","Facebook","Twitter","Linkldn","Jio")
# sentence1 = " ~~ ".join(listCompanies)
# sentence1= " and ".join(listCompanies)
# sentence1 = "\n".join(listCompanies)

# sentence2 = " and ".join(topComapnies)

# print(f"{sentence1} \nTop comapnies are --> {sentence2}")

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Format in python

# name = "Abhishek"
# company = "Walmart"
# role = "intern"

# str1 = f"Hello people, my name is {name} and the compant i am going to join as an intern in may 2022 is {company}"

# str2 = "Hello people, my name is {} and the compant i am going to join as an intern in may 2022 is {}".format(name,company)

# str3 = "Hello people, my name is {1} and the compant i am going to join as an {2} in may 2022 is {0}".format(company,name,role)

# print(str1)
# print(str2)
# print(str3)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# map , filter and reduce in python


# square = lambda x : x*x


# listArr = [1,2,4,7]

# mp = map(square,listArr)

# print(mp)
# print(list(mp))

# ------------------------------

# def numberGreaterThanFive(x):
#     return x>5

# listArr = [1,4,2,-5,45,6,2,89,7,5,90]
# arr = list(filter(numberGreaterThanFive,listArr))

# print(arr)

# from functools import reduce

# add = lambda a, b : a+b

# arr = [1,2,3,4]

# sum = reduce(add,arr)

# print(sum)

# --------------------------------------------------------------------------------------------------------------------------------------------









