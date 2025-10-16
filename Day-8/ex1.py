# from ourpack import calc
# fnum=float(input('Enter the first number:\t\t\t'))
# snum=float(input('Enter the second number:\t\t'))
# op=input('Choose operation: +\t-\t*\t/\t:\t')

# if(op=='+'):
#     print('Result of addition:\t',calc.add(fnum,snum))
# elif(op=='-'):
#     print('Result of subtraction:\t',calc.sub(fnum,snum))
# elif(op=='*'):
#     print('Result of multiplication:\t',calc.multi(fnum,snum))
# elif(op=='/'):
#     print('Result of division:\t',round(calc.div(fnum,snum),4))
# else:
#     print('Wrong operation choice, please try again')

#__________CODING WITH EXCEPTION
# print('\n--CODING WITH EXCEPTION--\n')
# from ourpack import calc
# try:
#     fnum=float(input('Enter the first number:\t\t\t'))
#     snum=float(input('Enter the second number:\t\t'))
#     op=input('Choose operation: +\t-\t*\t/\t:\t')

#     if(op=='+'):
#         print('Result of addition:\t',calc.add(fnum,snum))
#     elif(op=='-'):
#         print('Result of subtraction:\t',calc.sub(fnum,snum))
#     elif(op=='*'):
#         print('Result of multiplication:\t',calc.multi(fnum,snum))
#     elif(op=='/'):
#         print('Result of division:\t',round(calc.div(fnum,snum),4))
#     else:
#         print('Wrong operation choice, please try again')
# except ZeroDivisionError as ze:
#     print('Division by 0 is not allowed',ze)
# except ValueError as ve:
#     print('Error in the values',ve)
# except Exception as e:          # e can be replace, but recall same characters
#     print('Error!',e)
# finally:
#     print('Thank you, end of program')

#____________CODING WITH EXCEPTION & WHILE LOOP
print('\n--CODING WITH EXCEPTION & WHILE LOOP--\n')
from ourpack import calc
while True:
    try:
        fnum=float(input('Enter the first number:\t\t\t'))
        snum=float(input('Enter the second number:\t\t'))
        op=input('Choose operation: +\t-\t*\t/\t:\t')

        if(op=='+'):
            print('Result of addition:\t',round(calc.add(fnum,snum),4))
        elif(op=='-'):
            print('Result of subtraction:\t',round(calc.sub(fnum,snum),4))
        elif(op=='*'):
            print('Result of multiplication:\t',round(calc.multi(fnum,snum),4))
        elif(op=='/'):
            print('Result of division:\t',round(calc.div(fnum,snum),4))
        else:
            print('Wrong operation choice, please try again')
    except ZeroDivisionError as ze:
        print('Division by 0 is not allowed',ze)
    except ValueError as ve:
        print('Error in the values',ve)
    except Exception as e:          # e can be replace, but recall same characters
        print('Error!',e)
    choice=input('Do you want to continue? YES/NO:\t').lower()      # lower() is to detect either y or Y doesn't matter
    if(choice!='y'):
        print('Thank you, end of program')
        break
