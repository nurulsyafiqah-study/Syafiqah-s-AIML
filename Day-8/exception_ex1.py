#_________Normal coding without exception
fnum=float(input('Enter the first number:\t\t\t'))
snum=float(input('Enter the second number:\t\t'))
Div=fnum/snum
print(f'Result of dividing {fnum} and {snum} is:\t{round(Div,4)}')

#______Coding with exception
print('\n--CODING WITH EXCEPTION--\n')
try:
    fnum=float(input('Enter the first number:\t\t\t'))
    snum=float(input('Enter the second number:\t\t'))
    Div=fnum/snum
    print(f'Result of dividing {fnum} and {snum} is:\t{round(Div,4)}')
except Exception as e:
    print('Error',e)
finally:
    print('Thank you, end of program')