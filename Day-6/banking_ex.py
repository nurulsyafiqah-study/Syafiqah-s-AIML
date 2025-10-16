class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal
    def deposit(self,amount):
        self.bal+=amount
        print('Balance after deposit:\tRM',self.bal)
    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw:\tRM',self.bal)
        else:
            print('Insufficient amount in the account')
            print('Transaction failed')
    def show(self):
        print(f'Account Holder Name:\t{self.ac_holder}\tAccount Balance:\t{self.bal}')

ac=Account('NURUL SYAFIQAH BINTI HAKHIRUZZAMAN',15000)          #passing the value to the class's parameters
print('Please Choose:\n1. Deposit\t2.Withdraw\t')
choice=int(input())

if(choice==1):
    depo_amount=float(input('Enter amount to deposit:\tRM'))
    ac.deposit(depo_amount)
elif(choice==2):                                                #use elif untuk choose either choice and not print the else until none in the elif
    wd_amount=float(input('Enter amount to withdraw:\tRM'))
    ac.withdraw(wd_amount)
elif(choice==3):
    ac.show()
else:
    print('Wrong Choice')

#     def __init__(self,balance,ac_holder):
#         self.balance=balance
#         self.ac_holder=ac_holder

#     def get_balance(self):
#         return self.balance

# acc=Account(1000,'Sam')
# acc.balance=3400000
# print(acc.balance)