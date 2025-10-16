#1-WHILE LOOP EXAMPLE
# ourNum=int(input("Please enter the number you want to begin with: \t"))
# print(f'Printing Numbers from {ourNum} to 100')
# while(ourNum<=100):
#     print(f'{ourNum}',end="\t")
#     ourNum+=4


#2-BREAK EXAMPLE
# num=1
#print('Print Numbers from 1 to 100 before we get the numbers divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         num+=1
#         break
#     print(num,end="\t")
#     num+=1

#3-CONTINUE & WHILE LOOP EXAMPLE
# num=1
# while(num<=100):
#     if(num%2==1):       #IF TRUE, num+1 (will not print), if FALSE, will print
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1

#4-FOR LOOP
# for i in range(1,100):
#     if(i%5==0):
#         continue
#     print(i,end="\t")


correctPWD='girl'
counter=0
while True:
    pwd=input('Enter password to start the Game:\t')
    if(correctPWD==pwd):
        print('Welcome to the Game!')
        print("****Let's the game begin****")
        break
    else:
        print("Wrong password, please enter right password")
        counter+=1
        if(counter>=3):
            print("Account blocked, you have exceeded 3 password attempts")
            break