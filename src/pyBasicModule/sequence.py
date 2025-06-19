# seq : str, range, list, tuple, byte Array

## List
list = ["item1", 4, None, 'item2' , 3, None]
print(list.index(None))
# print(list.index("item9")) #ValueError: 'item9' is not in list

item_to_ignore = 'item4'
for item in list:
    if item == item_to_ignore:
        continue
    else:
        print(item)
print('-' * 50)

list2 = ["item1","item2","item3","item4","item5"]
item_to_find = 'item4'
for index in range(0,len(list2)):
    if list2[index] == item_to_find:
        print(list2[index], ' found !!')
        break
    else:
        print(list2[index], ' unmatched')

print('{}'.format(None))

