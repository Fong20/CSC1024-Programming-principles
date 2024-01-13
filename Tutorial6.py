#Tutorial 6
#Question1
#count = 0
#my_List = []
#while count < 5:
    #num = float(input("Enter a number:"))
    #my_List.append(num)
    #count +=1
#sorted arranges the value in ascending order
#print(sorted(my_List))

#Question2
#count = 0
#Total = 0
#my_List = []
#while count < 5:
    #num = float(input("Enter a number:"))
    #Total += num
    #my_List.append(num)
    #count +=1
#sorted arranges the value in ascending order
#print(sorted(my_List))
#print(f"Total = {Total}")
#Average = (Total / count)
#print(f"Average = {Average}")

#Question3
#count = 0
#forward_list = []

#while count < 5:
    #num = float(input("Enter a number:"))
    #forward_list.append(num)
    #count +=1

#print in ascending order
#print(f"forward_list = {sorted(forward_list)}")
#To print in descending order, make sure reverse = True
#print(f"reverse_list  = {sorted(forward_list, reverse = True)}")

#Question4
#count = 0
#my_List = []
#while count < 5:
    #num = float(input("Enter a number:"))
    #my_List.append(num)
    #count +=1

#print(f"my_List = {sorted(my_List)}")

#for _ in range(5):
    #print(sorted(my_List))
    #my_List.pop()
#print("[]")

#for _ in range(5):
    #print(sorted(my_List))
    #del my_List[-1]
#print("[]")

#Question 5
#count = 0
#my_List = []
#while count < 5:
    #num = input("Enter a data:")
    #my_List.append(num)
    #count +=1

#print(f"my_List = {sorted(my_List)}")

#for _ in range(5):
    #print(my_List)
    #my_List.pop()
#print("[]")

#Question 6
count = 0
my_List = []
while count < 5:
    num = input("Enter a number:")
    my_List.append(num)
    count +=1

#print(f"my_List = {sorted(my_List)}")
print(my_List)

while count >= 0:
    if count % 2 == 0:
        del my_List[count]
        print(my_List)   
    count -=1 
          
    #print("[]")
