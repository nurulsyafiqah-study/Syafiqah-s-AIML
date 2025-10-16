# username=input("Enter User Name \t") #\t is for tab for the space after command
# age=int(input("Enter age \t")) #integer
# salary=float(input("Enter Salary \t"))  #floating
# databaseKn=bool(input("Do you know databases? "))  #this is boolean

# print("Welcome Mr.\\Ms.",username)
# print("Your age is",age)
# print("Salary is ",salary)
# print("Do you know databases? ",databaseKn)

# #this command is for adding
# num1=int(input("First Number \t"))
# num2=int(input("Second Number \t"))
# sum=num1+num2
# print(f"Result of the sum of {num1} and {num2} = \t {sum}") #f is formatting

# #this command is for multiplication
# num1=int(input("First Number \t"))
# num2=int(input("Second Number \t"))
# multiplication=num1*num2
# print(f"Result of the multiplication of {num1} and {num2} = \t {multiplication}") #f is formatting

# #this command is for division
# num1=int(input("First Number \t"))
# num2=int(input("Second Number \t"))
# division=num1/num2
# print(f"Result of the division of {num1} and {num2} = \t {division}") #f is formatting


# #this command is for division% Remainder
# num1=int(input("First Number \t"))
# num2=int(input("Second Number \t"))
# Remainder=num1%num2
# print(f"Remainder after Dividing {num1} and {num2} = \t {Remainder}") #f is formatting

# num1=int(input("First Number \t"))
# num2=int(input("Second Number \t"))
#result=int(num1/num2)
#print(f"Result of the dividing of {num1} by {num2} = \t {result}") #f is formatting

#taking more than one input using single line
num1,num2=input("Enter two numbers separated by space ").split()
resultaddition=int(num1)+int(num2)
resultminus=int(num1)-int(num2)
resultdivision=int(num1)/int(num2)
resultmultiplication=int(num1)*int(num2)

print(f"Numbers entered by you are {num1} and {num2}")
print(f" and the addition of the numbers is {resultaddition}")
print(f" and the minus of the numbers is {resultminus}")
print(f" and the dividing of the numbers is {resultdivision}")
print(f" and the multiplication of the numbers is {resultmultiplication}")