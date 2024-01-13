#Tutorial 5
#Question 1

#decision = input("Enter N or n if you do not wish to continue to play the game:")

#while decision != 'N' or decision != 'n':
    #import random
    #secret_num = random.randint(1, 200)
    #guess_num = int(input("Guess my secret number: "))
    #count = 1 

    #while guess_num != secret_num:
        #if guess_num < secret_num:
            #print("Too Low")

        #elif guess_num > secret_num:
            #print("Too High")

        #count += 1
        #guess_num = int(input("Have another guess:"))

    #print(f"Well done, you took {count} attempts")
    #decision = input("Enter N or n if you do not wish to continue:")
#print("Thank you for playing the game.")

#Question 2
a = int(input("Which multiplication table would you like to print?"))
b = int(input("How high would you like it to go?"))
count = 1

print("Here is your multiplication table:")
while count <= b:
    result = a * b
    print(f"{a} times {b} = {result}")
    b -= 1
    count += 1

#Question 3
#Use list to list down the index of elements 
bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
count = 1

while count <= 5:
    #retrieving element from the list
    print(bits[0], bits[1], bits[2], bits[3], bits[4],bits[5], bits[6], bits[7], bits[8], bits[9], bits[10], sep = "")
    count +=1

#Question 4
print(f"[1] Convert Celsius to Fahrenheit")
print(f"[2] Convert Fahrenheit to Celsius")





while True:
    try:
        Selection = int(input("Enter your selection, 1 or 2:"))

    except:
        print("ERROR: Invalid Selection!")
        Selection = print("Please enter 1 to convert Celsius to Fahrenheit or 2 to Convert Fahrenheit to Celsius")

    else:
        while Selection == 1:
            print(f"Celsius (C) to Fahrenheit (F) Conversion")
            print(f"Enter temperature in integer values only.")
            min_temp = int(input("Enter minimum temperature:"))
            max_temp = int(input("Enter maximum temperature:"))
            Celsius = min_temp

            while min_temp <= max_temp:
                Fahrenheit = (Celsius * 9/5) + 32
                print(f"{min_temp}C = {Fahrenheit}F")
                min_temp +=1

            print("Conversion Done!")
            decision = input("Do you want to run the program again? [Y/N:]")
        
            if decision == "N":
                break

        while True:
            while Selection == 2:
                print(f"Fahrenheit (F) to Celsius (C) Conversion")
                print(f"Enter temperature in integer values only.")
                min_temp = int(input("Enter minimum temperature:"))
                max_temp = int(input("Enter maximum temperature:"))
                Fahrenheit = min_temp

                while min_temp <= max_temp:
                    Celsius = (Fahrenheit - 32) * 5/9
                    print(f"{min_temp}C = {Fahrenheit}F")
                    min_temp +=1

                print("Conversion Done!")
                decision = input("Do you want to run the program again? [Y/N:]")
    
                if decision == "N":
                    break





