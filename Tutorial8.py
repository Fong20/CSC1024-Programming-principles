#Tutorial 8 (functions)
#Question 1
#Define a user-defined function which prompts user to enter a number
#function name is number
def number():
    num = int(input("Enter a number:"))
    return num

#Define a user-defined function which counts from 1 to the number entered by the user
#function name is count
def count():
    for value in range(1, number() + 1):
        print(value)

#Invoke/call function
number()


count()

#Question 2
'''Define a user-defined function which will ask the user to pick a low and high number and generate a random number between the 2 values.
The values are then stored in a variable named comp_num'''

""" import random
def low_high_number():
    print("Enter a low number and a high number to generate a random number between the two values\n")
    low_number = int(input("Enter a low number:"))
    high_number = int(input("Enter a high number:"))

    comp_num = random.randint(low_number, high_number)
    return comp_num
    

def guess():
    print("I am thinking of a number...")
    guess_number = int(input("Guess the number:"))
    return guess_number

def result():
    while True:
        if guess_value == low_high_value:
            print("Correct, you win")
            break
        elif guess_value < low_high_value:
            print("Your guess is too low")

        else:
            print("Your guess is too high")

        guess()

        

low_high_number()
low_high_value = low_high_number()

guess()
guess_value = guess()


result() """

#Question3
#User input and calculation
""" user_num1 = int(input("Enter first number:"))
user_num2 = int(input("Enter second number:"))

user_addition = user_num1 + user_num2
user_subtraction = user_num1 - user_num2


import random

#addition function
def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)

    sum = num1 + num2
    return sum

#subtraction function
def subtraction():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)

    difference = num1 - num2
    return difference

#checking function
def checking():
    if user_addition == addition() or user_subtraction == subtraction():
        print("Correct")

    else:
        print(f"Incorrect, the answer is {addition()} for addition and {subtraction()} for subtraction")

#User menu 
print("[1] Addition")
print("[2] Subtraction")
print("[3] Checking")

#Prompt user to choose an option from the main menu
decision = input("Enter 1 or 2 or 3:")

#execute task when option is selected
if decision == "1":
    addition()
    print(f"the answer is {addition()}")

elif decision == "2":
    subtraction()
    print(f"the answer is {subtraction()}")

elif decision == "3":
    checking()

else:
    print("Please type in 1 or 2") """

#Question4
""" print("A program to find the maximum and  minimum numbers in a list")
user_list = []

def read_number():
    num_to_read = int(input("Enter how many numbers you want to read into the list:"))

    for _ in range(num_to_read):
        num = int(input("Enter a number:"))
        user_list.append(num)

    return user_list

def find_max_number():
    max_num = x [0]

    for num_List in x:
        if num_List > max_num:
            max_num = num_List
    
    print(max_num)

def find_min_number():
    min_num = x[0]

    for num_List in x:
        if num_List < min_num:
            min_num = num_List

    print(min_num)

read_number()

x = read_number()

find_max_number()

find_min_number() """



    

    

    




    