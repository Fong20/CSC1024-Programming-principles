#Tutorial 4 (while loop)
#Question 1
count = 0

print("Starting")
while count < 10:
    print(count, end = " ")
    count += 1

print("\nDone\n")

#Question 2
count = -20

print("Starting")
while count < 0:
    print(count, end = " ")
    count += 2

print("\nDone\n")

#Question 3
a = int(input("Please enter value of a:"))
b = int(input("Please enter vlaue of b:"))
result = a
i = 1

while i <= b:
    result *= result
    i += 1
print(f"value of {a} power {b} is {result}")
    
#Question 4
result = input("Enter any characters to perform sum of of unknown numbers 1 and 2 or type DONE to end the program:")

while result != "DONE":
    import random
    number1 = random.randint(1, 10)
    print(f"first unknown number is {number1}")
    number2 = random.randint(1, 10)
    print(f"second unknown number is {number2}")
    sum = number1 + number2
    print(f"the sum of unknown numbers is {sum}")

    #Control statement using user's input
    result = input("Enter DONE to end the program or continue")

#Question 5
secret_num = 50
count = 1

#Prompt user to guess value
guess = int(input("Please guess the value:"))

#When guess value is not the same as the secret num value, repeat the process
while guess != secret_num:

    if guess < 50:
        print("Your guess is too low.")

    elif guess > 50:
        print("Your guess is too high.")
    
    #Count how many times the user takes to guess the secret num value
    count += 1

    #Control statement using user input
    guess = int(input("Please guess the value:"))

#When the guess value is the same as the secret num value, print well done and how many counts taken
print(f"Well done, you took {count} attempts")


#While loop extra exercises
#Question 1
cont_loop = "y"

while cont_loop == "y":
    a = int(input("Enter value of first term (a):"))
    d = int(input("Enter value of common difference (d):"))
    n = int(input("Enter number of terms to be added (n): "))

    total = 0
    count = 0

#end='' is used to bring up all the answers to 1 line
    print("The terms in the arithmetic series are: ", end='')

    while count < n:
        #we use pass to tell Python to do nothing and go back to previous iteration
        #pass
        series_val = a + count * d
        total += series_val
        count += 1
        print(series_val, '', end='')

    print(f"\nSum of the first {n} terms are: {total} ")

#Control statement using user's input
    cont_loop = input("Please type y if you wish to continue of n if you do not wish to continue")

#Prompt user to retype inputs until it gets the correct input
#.lower converts the input to lower case
    while cont_loop.lower() != "y" and cont_loop.lower() != "n":
        cont_loop = input("Please type y if you wish to continue of n if you do not wish to continue")

#Question2
#Declare variables g,t and total
g = 32
t = 0
total_distance = 0

while t <= 10:
    #Calculate and print the distance
    d = 0.5 * g * (t ** 2)
    print(f"The distance the ball falls in {t} seconds interval is {d} ft")

    #Compound operator is used to obtain the total distance the golf ball falls at the end of each interval
    total_distance += d

    #Print out the total distance
    #\n is used to print the statement in new line
    print(f"Total distance the golf ball falls at end of {t} seconds is {total_distance} ft\n")

    #control statement
    t += 1

#Week 6 while loop exercise (on-page connector)
x = 21
sum = 0

while x <= 30:
    sum += x
    x += 1

#Calculate and print average upon exiting loop
avg = sum / 10
print(f"Average is {avg}")