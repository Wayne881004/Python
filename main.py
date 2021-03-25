# ch1
# name = input("what is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color)

#ch2
# birthday = input("input your birth year ")
# age = 2021 - int(birthday)
# print("Your age is " + str(age))
# print(type(birthday))

#ch3 String

# print('""') ##want to print ""
# course = 'Python for Beginners'
# another = course[:]
# print(course[-2])  
# print(course[0:2])
# print(course[2:-1])
# print(another)
# print(len(course))
#i = 2 
#print(course[0:i]) ##error

# CV = '''
# Hello,
# my name is bobo.

# '''
# print(CV) ##want to send email

#ch4
# weight = int(input("Weight = "))
# unit = input("(L)bs  or (K)g:")
# if unit.upper() == 'L':
#     print("You are {}pounds.".format(weight * 0.45))
# else:
#     print("You are {} pounds.".format(weight / 0.45))

# price = [10,20,30]
# total = 0 
# for item in price:
#     total += item
# print("total money : {}".format(total))
# for x in range(4):
#     for y in range(3):
#         print("{} {}".format(x,y))

# num = [5,2,5,2,2]
# for x in num:    
#     output = ""
#     for i in range(x):
#         output += "x" #print "F"
#     print(output)


# name = ['Bob','John']
# print(name[1])
# print(name)
# custom = {
#     "name" : "Bobo",
#     "age" : 30
# }
# custom["gender"] = "Male"
# print(custom["gender"])
# message = input(">")
# words = message.split(" ")
# emoji = {
#     ":)" : "😀",
#     ":(" : "😟"
# }
# output = ""
# for word in words:
#     output += emoji.get(word,word) + " "
# print(output)

# def square(number):
#     return number * number
# print(square(3))

# try:
#     age = int(input("Age: "))
#     print(200/age)
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# except ValueError:
#     print("Invalid value.")

# class Person:
#     #Constructors
#     def __init__(self, name):  #You can not only use "self", can change it.
#         self.name = name

#     def talk(self):
#         print("Hello, i am {}.".format(self.name))

# Bobo = Person("Bobo")
# print(Bobo.name)
# Bobo.talk()

# John = Person("John")
# print(John.name)
# John.talk()

# class Dog: #class member function needs to + "self"
#     def walk(self):
#         print("Walk.")

# class Cat(Dog):
#     pass 

# cat1 = Cat()
# cat1.walk()

#Ch6 Inheritance
# class Dog: 
#     def walk(self):
#         print("Walk.")

# class Cat(Dog):
#     def meow(self):
#         print("Meow.")
# cat1 = Cat()
# cat1.meow()
# cat1.walk()

#Ch7 model
# import lib
# print(lib.add(10,20))
# #equal------
# import lib
# from lib import add
# print(add(10,20))         


# import random as rd

# for i in range(3):
#     print(rd.random())
#     print(rd.randint(10,20))

# Member = ["Bob","Jack","Amy"]
# print(rd.choice(Member))
