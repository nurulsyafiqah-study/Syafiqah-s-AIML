print('DICTIONARY EXAMPLE')
ourDictionary=[
    {"id":'A',"name":'syafiqah',"age":'34'},
    {"id":'B',"name":'bella hadid',"age":'32'},
    {"id":'C',"name":'billie eilish',"age":'35'},
    {"id":'D',"name":'akshay',"age":'38'}
    ]

print('The IDs are:\t')
for keys in ourDictionary:
    print(keys['id'],end='| ')

print('\nThe NAMES are:\t')
for keys in ourDictionary:
    print(keys['name'],end='| ')

print('\nTheir ages are:\t')
for keys in ourDictionary:
    print(keys['age'],end='| ')

for k in ourDictionary:
    print(k['id']+'\t\t'+k['name']+'\t\t'+k['age'])