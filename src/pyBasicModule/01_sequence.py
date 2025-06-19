import data
print('Sequence manipulation', '_'*40)
menu = [
    ["boba tea", 'moon cake', 'spam'],
    ["boba tea", 'bun', 'casetella', 'spam'],
    ['moon cake', 'bun', 'casetella'],
    ["boba tea", 'moon cake', 'casetella'],
]
print('way 1 : printing list', '_'*40)
for meal in menu:
    # print(menu)
    for index in range(len(meal)-1, -1, -1):
        # print(index)
        if meal[index] == 'spam':
            # print('deleting ', menu[index] )
            del meal[index]
    print(meal)

print('\nway 2 : end key argument', '_'*40)
for meal in menu:
    for item in meal:
        if item != 'spam':
            # print(item, sep=' ',end=' ', file='sys.stdout', flush=False)
            # print(item, sep=", ")
            print(item, end=", ")
    print()

print('\nway 3, remove extra comma at end', '_'*40)
seperator =', '
for meal in menu:
    items=seperator.join(item if item != 'spam' else '' for item in meal)
    # items=seperator.join([item  for item in meal if item != 'spam'])
    # items = seperator.join(item for item in meal if item != 'spam')
    print(items)

print('JOIN','_'*40)
seperator =' | '
for meal in menu:items=seperator.join(meal); print(items)

print('SPLIT', '_'*40)
panagram="My name is \tAnna Liu, from california, irvine";
print(panagram.split()) # splits by space
print(panagram.split(',')) # splits by comma

numbers='1,2,3,45,6,78,89,10'
print(numbers.split()) # splits by space
print(numbers.split(',')) # splits by space

# prog to convert
print('\nPRG','_'*40)
panagram="My name is \tAnna Liu, from california, irvine";
l = list()
for char in panagram:
    if char == ',' or char == ' ' or char == '\t':
         pass
    else:
        l.append(char)

print(l)
l = '-'.join(l); print(l)
print(l.split('-'))

# in one line
print('-'.join( char for char in panagram if not (char == ',' or char == ' ' or char == '\t')).split('-'))

# Exercise
numbers = input('Enter 3 numbers, comma sepaerated')
numbers=numbers.split(','); print(numbers)
numbers=[int(n) for n in numbers]; print(numbers)
a,b,c= numbers; print(a, b, c)
print(a+b-c)


print(data.albums)








