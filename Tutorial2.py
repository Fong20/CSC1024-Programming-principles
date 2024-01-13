#Question 1
#Prompt user to enter the number of videos and oldies purchased
Number_Videos = int(input("Number of videos:"))
Number_Oldies = int(input("Number of Oldies:"))
Number_days = int(input("Number of days:"))

#Calculate the total charge for customer's video rental.
Total_charge = (((Number_Videos * 3.00) + (Number_Oldies * 2.00)) * Number_days)

#Print the total cost
print(f"Total cost is {Total_charge:.2f}")

#Question 2
#Prompt user to enter the time for an event in seconds
seconds = float(input("Time of event in seconds:"))

#Calculate hours
hours = seconds // 3600

remains = seconds - (3600 * hours)

#Calculate minutes
minutes = remains // 60

seconds = remains % 60

#Print out the time in hours, minutes and seconds
print(f"{hours:.0f}:{minutes:.0f}:{seconds:.0f}")

#Question 3
#Prompts user to enter his/her yearly income
yearly_income = float(input("Yearly income:"))

#If user's yearly income is between 0 and 2500, tax is 0
if yearly_income >= 0.0 and yearly_income <= 2500.0:
    tax = 0
    print(f"Amount of taxes to pay: {tax:.2f}")

#If user's yearly income is betweem 2501 and 10000, user has to pay 5% tax
elif yearly_income > 2500.0 and yearly_income <= 10000.0:
    tax = yearly_income * 0.05
    print(f"Amount of taxes to pay: {tax:.2f}")

#If user's yearly income is between 10001 and 50000, user has to pay 15% tax
elif yearly_income > 10000.0 and yearly_income <= 50000.0:
    tax = yearly_income * 0.15
    print(f"Amount of taxes to pay: {tax:.2f}")

#If user's yearly income is more than 50000, user needs to pay 25% tax.
else:
    tax = yearly_income * 0.25
    print(f"Amount of taxes to pay: {tax:.2f}")

#Question 4
#Prompt user to enter their monthly data usage
Monthly_usage = float(input("Monthly data usage in GB:"))

#Calculate and print the data charge for the month
if Monthly_usage <= 10.0:
    Charge = Monthly_usage * 15
    print(f"Data charges for the month is:{Charge:.2f}")

else:
    Charge = Monthly_usage * 30
    print(f"Data charges for the month is:{Charge:.2f}")

#Question 5
#Prompt user to choose R/r or C/c
Shape = input("Select rectangle or circle:")

#Calculate area of rectangle or area of circle
#If user inputs R or r, it will calculate and print the area of rectangle
if Shape == "R" or Shape == "r":
    length = float(input("Length of rectangle:"))
    width = float(input("Width of rectangle:"))

    area = length * width

    print(f"Area of rectangle is {area:.2f}")

#If user inputs C or c, it will calculate and print the area of circle
elif Shape == "C" or Shape == "c":
    PI = 3.14159
    radius = float(input("radius of circle:"))

    area = (PI * (radius**2))

    print(f"Area of circle is {area:.2f}")

else:
    print("Please enter R or r or C or c")

#Question 6
#Prompt user to enter day of the week in number
day = int(input("Please enter day of the week in number:"))

#Use match case to print out the output based on the user's input
match day:
    case 1:
        print(f"The drink of the day is Peppermint Mocha")

    case 2:
        print(f"The drink of the day is Candy Bar Latte")

    case 3:
        print(f"The drink of the day is Caramel Coffee")

    case 4:
        print(f"The drink of the day is Chocolate Almond Cafe Au Lait")

    case 5:
        print(f"The drink of the day is Pumpkin-Chai Latte")
    
    case 6:
        print(f"The drink of the day is Vanilla-Chai Tea")
    
    case 7:
        print(f"The drink of the day is Gingerbread Latte")
    
    case _:
        print("Please enter values from 1 to 7")