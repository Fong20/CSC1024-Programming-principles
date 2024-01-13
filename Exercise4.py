#Prompt user to enter length of rectangle
length = float(input("Please enter length of rectangle (cm): "))

#Prompt user to enter height of rectangle
height = float(input("Please enter height of rectangle (cm): "))

#Calculate the area of rectangle
Area_of_Rectangle = (length * height)

#Calculate the perimeter of rectangle
Perimeter_of_Rectangle = ((2 * length) + (2 * height))

#Print area of rectangle and perimeter of rectangle
print("Area of rectangle is " , Area_of_Rectangle, "cm")
print("Perimeter of rectangle is " , Perimeter_of_Rectangle, "cm")