#Prompt user to enter amount in RM
Amount_RM = float(input("Please enter RM in amount: "))

#Fixed exchange rate of 3.04
Exchange_Rate = 3.04

#Calculate amount in SGD
Amount_SGD = Amount_RM / Exchange_Rate

#Print amount in SGD, round to 2 decimal point
print("Your amount in SGD is: ", round(Amount_SGD , 2))
