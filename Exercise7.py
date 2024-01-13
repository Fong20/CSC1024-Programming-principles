#prompt user to enter total price of bill
bill = float(input("Please enter total of the bill: "))

#prompt user to enter number of friends
friends = int(input("Please enter number of friends: "))

#calculate total price of bill including service tax and GST
total = round(bill + (bill * 0.1) + (bill * 0.06) , 2)

#calculate amount needed to be paid by each friend
payment = round(total / friends , 2)

#print amount needed to be paid by each friend
print("Amount to be paid by each friend is " , payment)