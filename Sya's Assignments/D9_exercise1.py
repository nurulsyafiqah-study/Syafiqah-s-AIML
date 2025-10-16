# Write a program using functions to find greatest of three numbers entered by user
# Write the solution in Assignments folder with name
# day_9_ex1.py
# Push on GitHub
# Share GitHub link in chat once done
num1=int(input('Please enter number 1:\t'))
num2=int(input('Number 2:\t'))
num3=int(input('Number 3:\t'))

def find_max(num1,num2,num3):
    return max(num1,num2,num3)

print(f"The greatest numbers of {num1}, {num2}, {num3} you've entered is:\t",find_max(num1,num2,num3))
    

