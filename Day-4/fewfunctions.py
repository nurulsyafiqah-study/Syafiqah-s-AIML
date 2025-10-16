# def factorial(num):
#     if((num==0)or(num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
    
# num=int(input('Enter a number to find the factorial of the number: \t'))
# print(f'Factorial of {num} is\t:\t',factorial(num))class
    


#___________TASK
#__________WRITE A PYTHON FUNCTION WHICH CONVERTS INCHES TO CM
# 1inch=2.54cm

# print('CONVERTING INCH TO CM')
# inputInch=float(input('\nInch to Convert\t:\t'))
# def convert(inputInch):
#     return inputInch*2.54

# print(f'{inputInch} inch =\t{convert(inputInch)} cm')


#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter number to find out the table\t:\t'))
gen_table(number)