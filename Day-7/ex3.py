#________________________PRINTING DATE & TIME_______________________
import datetime
import inspect
dtclasses=inspect.getmembers(datetime,inspect.isclass)

print('All Classes in datetime module')
for n,func in dtclasses:
    print(n,end='\t')

print("\n--------Today's date--------\n")
print(datetime.date.today().strftime("%B %d, %Y"))

print('\n--------Current Date & Time--------\n')
print(datetime.datetime.now())
print('\n--------Current Time--------\n')
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formattedtime=datetime.datetime.now().strftime('%I:%M:%S %p')

print('Current Time\t',cttime)
print('Formatted Time\t',formattedtime)