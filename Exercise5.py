#prompt user to enter mass of object
Mass = float(input("Please enter object's mass: "))

#prompt user to enter velocity of object
Velocity = float(input("Please enter object's velocity: "))

#calculate momentum of object               
Momentum = round(Mass * Velocity , 2)

#calculate kinetic energy of object
Kinetic_Energy = round(1/2 * Mass * Velocity ** 2 , 2)

#Print momentum and kinetic energy of object
print("The momentum of object is: " , Momentum)
print("The Kinetic Energy of object is: ", Kinetic_Energy)

