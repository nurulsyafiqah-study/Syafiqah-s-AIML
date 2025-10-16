# print('Write a function to find out the cube of given number')
# #5 : 5*5*5 (eg cube of 5 is 5*5*5 = 125

# def cube(num):
#     return num*num*num
# num1=int(input('Enter the number to find the cube of it:\t'))           #float for decimals, int for whole number
# print(f'The cube of {num1} is: \t',num1*num1*num1)



#write a function to find out bonus of given salary
#function take salary as input and return bonus (10% of salary)

print('TASK 2: write a function to find out bonus of given salary')

salary=float(input('\nPlease enter the salary to find out the bonus and total salary include bonus: \t'))
def bonus(salary):
    return salary*0.1
def newsalary(salary):
    return salary+bonus(salary)
print('Your bonus is\t\t\t\t\t\t: \t\t',round(bonus(salary)),2)
print('The total salary this month (including bonus) is\t: \t\t',round(newsalary(salary),2))
print(f'Salary is:\t{salary}  \tbonus is:\t{bonus(salary)}')