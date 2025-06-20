# A. String
name="1. Hello Liu"; print(name); print(name[:6]+name[6:] + name[:]) #dont include index 6
name="2. Hello Liu!! 'How are You'"; print(name)

n="0123456789" ; print(n[9] , n[-1], n[9-10], n[-6:-1:2]) # positive index - lenght : 3rg: Step
n="_1234+1234_1234?1234" ; print(n[0:n.__sizeof__():5])
seperator = n[0::5] ; print(seperator); # prepare seperator way 1
for i in n: # prepare seperator way 2
    #print(type(i))
    if not i.isnumeric():
        seperator = seperator + i
value = "".join(char if char not in seperator else " " for char in n).split();

# see ways to print
print(int(v) for v in value) #enerator object <genexpr> at 0x7f8e1ee82890
print([int(v) for v in value])
for v in value:
    print(v)

#backslicing
letter='abcdefghijklmnopqrstuvwxyz';
print('back Slicing', letter[25:-1:-1], " | ", letter[25:25:-1]); #same, using negative indexing
print('back Slicing', letter[25:-2:-1], " | ", letter[25:24:-1]); #same, using negative indexing
print('back Slicing', letter[25::-1]); #end in 0, if negative step
print('back Slicing', letter[::-1]); #end in 0, if negative step n start is max index
print('back Slicing challenge : last 8 : ', letter[25:-9:-1])
print('back Slicing challenge : qpo: ', letter[-10:-13:-1], ' ,edbca:' , letter[4::-1])


liu = "3. \nAnna"; dinkar="\tlekhraj"
print(liu+ ' '+ dinkar)

print(554); print(5*4); print()

# triple quotes
text="""4. Hello Liu!! 
what are u doing 
'How are You'  """; print(text)

text="hello \"My name is lekhraj\" "; print(text)

print("Pet clinic by \"Spring boot\" ")
#or
print('Pet clinic by "Spring boot"')

print(r"C:\Users\tim\nice"); print("C:\\Users\\tim\\nice")

#friend = input("Who is your best friend ?"); print(friend);

letter='abcdefghijklmnopqrstuvwxyz';
print(letter[25:27])

# String fnction... check doc
print("aBc".capitalize())
print("aBc".swapcase())
print("aBc".casefold()); print("ABC".isupper());









