#___________________PRINTING RANDOM NUMBER___________________________________
# import random
# print('Random Number from 1 to 1000')
# print(random.randint(1,10))

#____________________________________________________________________________
print('\t\t\tWELCOME TO LUCKY DRAW CONTEST!\n')
import random
name=input('Enter Your Name:\t')
luckyNumber=random.randint(1,10)
print(f'Welcome Mr./Ms. {name}\tCoupon Number:\t{luckyNumber}')
if(luckyNumber==1):
    print('Congrats!! You have won Proton E-mas')
elif(luckyNumber==3):
    print('Congrats!! You have won an Iphone 20 Pro Max')
elif(luckyNumber==10):
    print('Congrats!! You have won a Google TV 65"')
else:
    print('Better luck next time ;)')
