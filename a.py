# ch1
# name = input("what is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color)

#ch2
# birthday = input("input your birth year ")
# age = 2021 - int(birthday)
# print("Your age is " + str(age))
# print(type(birthday))

#ch3
weight = int(input("Weight = "))
unit = input("(L)bs  or (K)g:")
if unit.upper() == 'L':
    print("You are {}pounds.".format(weight * 0.45))
else:
    print("You are {} pounds.".format(weight / 0.45))