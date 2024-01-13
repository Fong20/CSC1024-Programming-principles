#declare constant PI VALUE
PI_VALUE = 3.142

#prompt user to enter radius of sphere
radius = float(input("Please enter radius of sphere: "))

#calculate diameter of sphere 
diameter = round(2 * radius , 2 )

#calculate circumference of sphere
circumference = round(2 * PI_VALUE * radius , 2)

#calculate  surface area of sphere
surface_Area = round(4 * PI_VALUE * radius ** 2 , 2)

#calculate volume of sphere
volume = round(4/3 * PI_VALUE * radius ** 3 , 2)

#print radius, circumference, surface area and volume of sphere
print("The radius of sphere is " , radius)
print("The circumference of sphere is " , circumference)
print("The surface area of sphere is " , surface_Area)
print("The volume of sphere is " , volume)