try:
    num1=float(input('Enter first number:\t'))
    num2=float(input('Enter second number:\t'))
    total=num1+num2
    print(f'Sum of {num1} and {num2} = {total}')
except Exception as e:
    print('Error',e)
finally:
    print('End of the Program')