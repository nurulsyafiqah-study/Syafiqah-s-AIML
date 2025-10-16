print('TUPLE TOPICS HERE')
# subjects=('python','java','dotnet','sql','html','numpy','powerbi')
# print('All subjects are: \n')
# print('Total Subjects are: ',len(subjects))
# for subjectList in subjects:
#     print(subjectList,end='\t')

#____________
# numbers=(1,2,3,4,5,6,7,8,9,1,2,10,1,11,12,13,14,15)
# print('Total number in tuple: ',len(numbers))
# for num in numbers:
#     print(num,end='\t')

#______________tupleName.index(item) will return the index of first occurance of item in tupleName
# search_num=int(input('\nEnter number to find the index: \t'))
# if search_num in numbers:
#     print(f'Index of {search_num} is: \t',numbers.index(search_num))
# else:
#     print(f'{search_num} is not in the tuple')


#______________tupleName.count(item): will count the number of times of item occurance in tupleName
# search_num=int(input('\nEnter number to find the FREQUENCY: \t'))
# if search_num in numbers:
#     print(f'Searched number: {search_num} \nThe occurance is: {numbers.count(search_num)} times')
# else:
#     print(f'{search_num} is not in the tuple')



#TASK 1______________WRITE A PROGRAM TO SUM A LIST WITH 4 NUMBERS______________
print("TASK 1: WRITE A PROGRAM TO SUM A LIST WITH 4 NUMBERS")
taskNumber1=(87,38,91,34)
for numbers in taskNumber1:
    print(numbers)
total=sum(taskNumber1)
print(f'The sum of the numbers are {total}')