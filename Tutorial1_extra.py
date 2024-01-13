#Question 1
Total_cookies = int(input("Total number of cookies:"))
Cookies_Box = int(input("Number of cookies in a box:"))
Cookies_Container = int(input("Number of cookie boxes in a container:"))

Number_boxes = Cookies_Box // 24
Number_Containers = Number_boxes // 75

Leftover_cookies = Cookies_Box % 24



#Question 2
#Prompt user to input two integers and operation to be performed
Number1= int(input("Enter first integer:"))
Number2 = int(input("Enter second integer:"))
Operator = input("Enter your operator:")

if Operator == "+":
    Output = Number1 + Number2
    print(f"{Number1} {Operator} {Number2} = {Output}")

elif Operator == "-":
    Output = Number1 - Number2
    print(f"{Number1} {Operator} {Number2} = {Output}")

elif Operator == "*":
    Output = Number1 * Number2
    print(f"{Number1} {Operator} {Number2} = {Output}")

elif Operator == "/":

    if Number2 == 0:
        print("The fraction is undefined as the denominator is 0")
    
    else:
        Output = Number1 / Number2
        print(f"{Number1} {Operator} {Number2} = {Output}")

else:
    print("Please enter a valid operator")
    
#Question3
#Prompt user to enter the net price of each copy of novel and estimated copies that will be sold
net_Price = float(input("Net price of novel:"))
copies = int(input("Number of copies of novel:"))

#Calculates royalty of option 1   
#Author is paid 5000 upon delivery of final manuscript and 20000 when the novel is published     
option1 = 5000.0 + 20000.0
print(f"Royalty for option 1 is {option1:.2f}")

#Calculates royalty of option 2
#Author is paid 12.5% of net price of novel for each copy of novel sold
option2 = ((net_Price * 0.125) * copies)
print(f"Royalty for option 2 is {option2:.2f}")

#Calculates royalty of Option 3
#Author is paid 10% of net price for the first 4000 copies
if copies > 0 and copies <= 4000:
    option3 = net_Price * 0.10
    print(f"Royalty for option 3 is {option3:.2f}")

#Author is paid 14% of net price for more than 4000 copies
else:
    option3 = net_Price * 0.14
    print(f"Royalty for option 3 is {option3:.2f}")

#Prints out the best option the author could choose
#If the output of option 1 is larger than output 2 and output 3, print author could choose option 1
if option1 > option2 and option3:
    print("The best option the author could choose is option 1")

#If the output of option 2 is larger than output 1 and output 3, print author could choose option 2
elif option2 > option1 and option3:
    print("The best option the author could choose is option 2")

#If the output of option 3 is larger than output 1 and output 2, print author could choose option 3
elif option3 > option1 and option2:
    print("The best option the author could choose is option 3")

#Question4
#Promt user to enter the cost of renting one room, discount of each room as percent,number of rooms booked, number of days booked, total cost of rooms, sales tax and total billing amount
cost_Room = float(input("Cost of renting one room:"))
number_Room = int(input("Number of rooms booked:"))
nights = int(input("Number of days the rooms are booked:"))
sales_Tax = float(input("Amount of sales tax in percent:"))

if number_Room >= 0 and number_Room < 10:
    print(f"Cost of renting one room is {cost_Room}")

    Discount = 0 // number_Room
    print(f"Discount on each room is {Discount} %")

    print(f"The number of days the rooms are booked is {nights}")

    total_Cost = (cost_Room * number_Room * nights)
    print(f"The total cost of the rooms is {total_Cost:.2f}")

    print(f"The sales tax is {sales_Tax:.2f} %")

    total_Bill = (total_Cost + (total_Cost * (sales_Tax / 100 )) - (total_Cost * (Discount / 100)))
    print(f"The total billing amount is {total_Bill:.2f}")

elif number_Room >= 10 and number_Room < 20:
    print(f"Cost of renting one room is {cost_Room}")
    
    if nights >=3:
        Discount = 15 // number_Room
        print(f"Discount on each room is {Discount} %")
    
    else:
        Discount = 10 // number_Room
        print(f"Discount on each room is {Discount} %")

    print(f"The number of rooms booked is {number_Room}")

    print(f"The number of days the rooms are booked is {nights}")

    total_Cost = (cost_Room * number_Room * nights)
    print(f"The total cost of the rooms is {total_Cost:.2f}")

    print(f"The sales tax is {sales_Tax:.2f} %")

    total_Bill = (total_Cost + (total_Cost * (sales_Tax / 100 )) - (total_Cost * (Discount / 100)))
    print(f"The total billing amount is {total_Bill:.2f}")

elif number_Room >= 20 and number_Room < 30:
    print(f"Cost of renting one room is {cost_Room}")
    
    if nights >= 3:
       Discount = 25 // number_Room
       print(f"Discount on each room is {Discount} %")
    
    else:
        Discount = 20 // number_Room
        print(f"Discount on each room is {Discount} %")

    print(f"The number of rooms booked is {number_Room}")

    print(f"The number of days the rooms are booked is {nights}")

    total_Cost = (cost_Room * number_Room * nights)
    print(f"The total cost of the rooms is {total_Cost:.2f}")

    print(f"The sales tax is {sales_Tax:.2f} %")

    total_Bill = (total_Cost + (total_Cost * (sales_Tax / 100 )) - (total_Cost * (Discount / 100)))
    print(f"The total billing amount is {total_Bill:.2f}")

else:
    print(f"Cost of renting one room is {cost_Room}")
    
    if nights >= 3:
       Discount = 35 // number_Room
       print(f"Discount on each room is {Discount} %")
    
    else:
        Discount = 30 // number_Room
        print(f"Discount on each room is {Discount} %")

    print(f"The number of rooms booked is {number_Room}")

    print(f"The number of days the rooms are booked is {nights}")

    total_Cost = (cost_Room * number_Room * nights)
    print(f"The total cost of the rooms is {total_Cost:.2f}")

    print(f"The sales tax is {sales_Tax:.2f} %")

    total_Bill = (total_Cost + (total_Cost * (sales_Tax / 100 )) - (total_Cost * (Discount / 100)))
    print(f"The total billing amount is {total_Bill:.2f}")