#prompt user to enter 5 test scores

test_Score1 = float(input("Please enter test score 1: "))
test_Score2 = float(input("Please enter test score 2: "))
test_Score3 = float(input("Please enter test score 3: "))
test_Score4 = float(input("Please enter test score 4: "))
test_Score5 = float(input("Please enter test score 5: "))

#Calculate average test score
average_Score = test_Score1 + test_Score2 + test_Score3 + test_Score4 + test_Score5

#print average test score, answer is rounded to 2 decimal space
print("Average test score is " , round(average_Score , 2))

