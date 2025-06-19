import data
import print_color

config = data.config_dict;

print(config.get('os'), config.get('OS', 'Not found OS. Did you mean os ?')) # if key not, None with get . it is faster
print(config['os']);  # print(config['OS']) # if key not found keyError

print('-'*50)
for key in config:
    print( key, config[key], sep=', ')

print('-'*50) # order is maintained after P-3.5
for index, key in enumerate(config):
    print(index, key, config[key] )

print('UPDATE, ADD, POP','-'*50)
config['memory'] = '8GB' # update
config['cpu'] = 'intel core i9' # add
config.setdefault('ram','2gb') #add


del config['model'] #delete| other way : config.pop('model')
# del config['model1'] #delete failed here, model1 not exists
print(config.pop('os'), 'has been delted') # pop return deleted value
print(config.pop('os', 'OS feilds already deleted')) # if key not found, retyrn any type in 2nd arg

print('-'*50)
# IMP : item() will return list of tuple like (k,v). use dict fn to convert it to dict.
print(config.items(), '\n',sorted(config.items()) ) #sorting dictionary
def print_config():
    for  key,value in sorted(config.items()): # items create list and use extra menory.
        print(key.center(20), value, sep=' : ')
    return key.center(20), value, ':-)'


print(type(config.items()))

# PROGRAM
print_color.myPrintWithMoreEffect('Please enter choice : add/a, pop/p or info/i. e/exit', print_color.UNDERLINE, print_color.BOLD, print_color.GREEN)
choice = None
while choice != 'e':
    x,y,z = print_config(); print(z)
    choice = input(" >> choice (i,a,p,e/exit) >> ")
    if(choice == 'a'):
        key = input("Enter key: "); value = input("Enter value : ")
        config[key] = value

    elif(choice == 'p'):
        key = input("Enter key: ")
        print(config.pop(key, 'Key not Found... try again !!'))

    elif(choice == 'i'):
        choice = input("Enter key:")
        print_color.myPrintWithMoreEffect(config.get(choice), print_color.UNDERLINE, print_color.BOLD, print_color.GREEN)

    elif (choice == 'e'):
        break

    else:
        print_color.myPrintWithMoreEffect('Wrong Choice', print_color.UNDERLINE, print_color.BOLD,
                                          print_color.RED)
        print_color.myPrintWithMoreEffect('valid choice : add, pop or info', print_color.UNDERLINE,
                                          print_color.BOLD, print_color.GREEN)
