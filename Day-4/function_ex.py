#default parameter in function
# def info(id,name,city='KL'):
#     print(f'Details as follows \nID: {id} \nName: {name} \nCity: {city}')

# info(1,'Sya','New Delhi')
# info(101,'Xi')
# info(103,'Chang')

#we want to create a single method that can able to add 2 numbers,3 numbers,4 numbers or numbers
#and return correct total

def add(n1,n2=0,n3=0,n4=0,n5=0):                #limited parameters (5 only)
    return n1+n2+n3+n4+n5
print('Result:\t',add(1,2))
print('Result:\t',add(5,3,1,4,10))
print('Result:\t',add(5,25,10))

def p(*numberless):
    return sum(numberless)

print('Sum of 2,3,4 is:\t',p(2,3,4))


#_____________MAXIMUM, MINIMUM, AVERAGE

print('Maximum Example')
print('Max of 1,10,11 is:\t',max(1,10,11))
print('Max of 5,2 is:\t',max(5,2))
print('Max of 10,10,100,100,200,219,19 is:\t',max(10,10,100,100,200,219,19))
 
print('Minimum Example')
print('Min of 1,10,11 is:\t',min(1,10,11))
print('Min of 5,2 is:\t',min(5,2))
print('Min of 10,10,100,100,200,219,19 is:\t',min(10,10,100,100,200,219,19))
 
print('Average Example')
print('Avg of 1,10,11 is:\t',avg(1,10,11))
print('Avg of 5,2 is:\t',avg(5,2))
print('Avg of 10,10,100,100,200,219,19 is:\t',avg(10,10,100,100,200,219,19))


 