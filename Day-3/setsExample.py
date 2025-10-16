# print('SETS IN PYTHON')
# set_one={'laptop','iPhone','headphone','mouse','keyboard','laptop','headphone'}     #it will not print the duplicate ones
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item)


#___________clear(): remove all the items from set
# set_one.clear()
# print('After clear, number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item)


#___________set.remove(item): updates the set and remove the item from the set
# set_one.remove('laptop')
# print('\nAfter removing "laptop" from the set: ',len(set_one))
# for item in set_one:
#     print(item,end="\t")

#saje2 try
# remove=(input'Item to be removed: \t')
# set_one.remove(f(remove))
# print('\nAfter removing "laptop" from the set: ',len(set_one))
# for item in set_one:
#     print(item,end="\t")


#___________union, intersection,difference
# set_one={100,200,300,400,500,600,700}
# set_two={100,400,800,1200}
# set_three={100,2,3,4}

#_________union
#s1.union(s2): returns new set with all items from both sets s1,s2
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)}')
# print(set_two)

# unionset=set_one.union(set_two,set_three)
# print(f'Union of set_one and set_two contains: {len(unionset)}  following items')

# print(unionset)



#________intersection example
#s1.intersection(s2): returns set which contains only item in both sets s1,s2,s3
# set_one={100,200,300,400,500,600,700}
# set_two={100,400,800,1200}
# set_three={100,2,3,4}

# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)}')
# print(set_two)
# print(f'set_three contains: {len(set_three)}')
# print(set_three)

# intersecSet=set_one.intersection(set_two,set_three)
# print(f'Intersection of set_one, set_two and set_three contains: {len(intersecSet)}  following items')

# print(intersecSet)


#________difference example
#s1.difference(s2): return set which contains only item in s1 but not in s2 (which contains those that is not common in all sets)
set_one={100,200,300,400,500,600,700}
set_two={100,400,800,700,1200}
set_three={100,2,3,4,700}

print(f'set_one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)}')
print(set_two)
print(f'set_three contains: {len(set_three)}')
print(set_three)

differenceSet=set_one.difference(set_two,set_three)
print(f'Difference of set_one, set_two and set_three contains: {len(differenceSet)}  following items')

print(differenceSet)