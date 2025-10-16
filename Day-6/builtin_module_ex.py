# import math
# import random

# mynum=int(input('Enter number to find out the square root:\t'))
# print(f'Square root of {mynum} is:\t',math.sqrt(mynum))

# print('Your lucky Number from 1 to 100 is:\t',random.randint(1,100))
#_________________________________________________________________________________________________________________________


#________TO CHECK FUNCTION INSIDE THE MODULE
import math
import inspect
functions=inspect.getmembers(math,inspect.isbuiltin)
for n, func in functions:
    print(n)
print('Sin 90 is:\t',math.sin(90))