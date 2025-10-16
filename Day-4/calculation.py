def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

print('Welcome to our calculator')
while True:
    print('Select Operation \n1. Add \n2. Substraction \n3. Multiplication \n4. Division \n5. Average \n6.Exit')
    op=int(input('Enter your operation of your choice (1-6): \t'))
    if(op==6):
        print('GoodBye')
        break
    if((op>=6) or (op<=1)):
        print('Wrong operation choice')
    else:
        fnum=float(input('Enter first number:\t'))
        snum=float(input('Enter second number:\t'))

        if(op==1):
            print(f'Result of addiotional of {fnum} and {snum}:\t',add(fnum,snum))
        if(op==2):
            print(f'Result of substraction of {fnum} and {snum}:\t',sub(fnum,snum))
        if(op==3):      #can use elif 
            print(f'Result of multiplication of {fnum} and {snum}:\t',multi(fnum,snum))
        if(op==4):
            print(f'Result of division of {fnum} and {snum}:\t',div(fnum,snum))
        if(op==5):
            print(f'Result of average of {fnum} and {snum}:\t',avg(fnum,snum))
 
        
               