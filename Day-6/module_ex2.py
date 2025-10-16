# import datetime
# import inspect
# print('Today is:\t',datetime.date.today())

# dtclasses=inspect.getmembers(datetime,inspect.isclass)
# print('All Classes inside datetime module')

# for n, func in dtclasses:
#     print(n)

# print('All functions inside datetime.date class')

# functions=inspect.getmembers(datetime.date,inspect.isbuiltin)
# for n,func in functions:                                    #func is what's already in the computer's functions, it will list all functions
#     print(n)

#__________________________________________________________________________________________________________


import os               #     os is a module
#import inspect
#functions=inspect.getmembers(os,inspect.isbuiltin)
listDirs=os.listdir()
for dr in listDirs:
    print(dr)