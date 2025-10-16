#def function_name(parameters):
#        '''Docstring'''
#           statement(s)

#_____________THIS IS FUNCTION WITHOUT PARAMETERS
# def welcome():                          #storing the data in container welcome
#     print("Welcome to functions")

# def saya():                             #storing the data in container saya
#     print('saya cuba coding')

# welcome()           #FUNCTION calling it can be many times
# welcome()
# saya()
# welcome()



#_____________THIS IS FUNCTION WITH A PARAMETER
def welcome(m):
    print('Welcome to functions in python Ms./Ms. ',m)

username=input('Please enter your name: \t')

welcome(username)

#_____________THIS IS FUNCTION WITH A PARAMETER AND RETURN

#def add()= addition+
#def multi()= multiplication*
#def 
def add(num1,num2):        
    return num1+num2
fnum=int(input("Enter first number: \t"))
snum=int(input('Enter second number: \t'))
print(f'Result after adding {fnum} and {snum} is= \t',add(fnum,snum))