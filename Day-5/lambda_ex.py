# def add(a,b):
#     total=a+b
#     return total

# result = add(12,15)
# print(result)


#THIS IS THE FORMULA
addition = lambda a,b:a+b
darab=lambda a,b:a*b
bahagi=lambda a,b:a/b
average=lambda a,b:(a+b)/2
tolak=lambda a,b:(a-b)

#THIS IS WHERE YOU REQUEST INPUT
number1=int(input('Enter number 1:\t'))
number2=int(input('Enter number 2:\t'))

# print(addition(a,b))
print('\nTHE RESULTS ARE\t:')
print('Addition = ',addition(number1,number2))
print('Multiplication = ',darab(number1,number2))
print('Division = ',bahagi(number1,number2))
print('Average = ',average(number1,number2))
print('Substraction = ',tolak(number1,number2))


#check_even=lambda x: "even"
check_odd = lambda n:'Odd number' if n%2==1 else 'Even number'
num1=int(input('Enter number to check ODD or EVEN :\t'))
print(check_odd(num1))