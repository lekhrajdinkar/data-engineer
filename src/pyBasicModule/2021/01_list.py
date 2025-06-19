import data

print('module name: ', __name__)
l = [1,2,3,4]; print('original array ',l);

l = l + [5]; print('original array + [5] ',l);
l.append(6); print('original array.append(6) ',l); # ADD
l[len(l)-1] = 666 ; print('original array, index to next index ',l); # ADD # UPDATE
del l[3:]; print('original array, del l[3:] ',l); # ADD
