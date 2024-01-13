#Question1
#num= int(input("Enter a number:"))
#for i in range(1,12):
    #print(f"The multiplication table of {num} is {i} x {num}")
    

#Question2
#num = int(input("Enter a number:"))
#range(start, stop, step up/step down)
#for i in range(50, num-1, -1):
    #print(f"{i}")

#Question3
#decision = input("Please select up or down")

#if decision == "up":
    #top_num = int(input("Please enter a top number:"))

    #for i in range(1, top_num+1):
        #print(f"{i}")

#elif decision == "down":
    #down_num = int(input("Please enter a number below 20:"))

    #if down_num < 20:
        #for i in range(20, down_num-1, -1):
            #print(f"{i}")

    #else:
        #print("I don't understand")

#else:
    #print("I don't understand")

#Question4
import random
score = 0

for total_questions in range(1,6):
    #Generate 2 random numbers from 1 to 10
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    #Generate 5 questions by adding the 2 random numbers together
    question = num1 + num2

    #Prompt user to enter the answer 5 times
    answer = int(input("Please enter the answer:"))
    
    #If the answer is correct, user gains a point to their score
    if answer == question:
        score +=1
        #print(f"Your point is {score}")

#Print the final results after answering 5 questions    
print(f"Your results are: {score}/{total_questions}")

#Question6
print("A program to find the maximum and  minimum numbers in a list")
print("Enter ten (10) numbers into a list")
my_list = []
for _ in range(10):
    num = float(input("Enter a number:"))
    my_list.append(num)

print(my_list)
print(max(my_list))

#num_max, num_min = my_List[0], my_list[0]
#for num_list in my_list:
    #if num_list > num_max:
        #num_max = num_list
    
    #if num_list < num_min:
        #num_min = num_list

















