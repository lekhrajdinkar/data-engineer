from data import albums

# Tuple - seq type, immujtable
l = ['ABC', 'DEF', 42] ; print(l)
t = ('ABC', 'DEF', 42 ); print(t)
t = 'ABC', 'DEF', 42 ; print(t) # can omit parenthesis

print('ABC', 'DEF', 42 ); print(('ABC', 'DEF', 42 )) # always use parenthesis while using tuple as method argument

# indexing is same t[0]
# t[0] = "ABCDE" # TypeError: 'tuple' object does not support item assignment

# unpacking
x,y,z = (10,20,30)
x,y,z = 10,20,300
x,y,z= t
x,y,z= "xyz" # can unpack any sequence type

# l.append('11') ; x,y,z= l # can unpack any sequence type. Break therefore tuple are better for unpacking
print(x,y,z)

for i, value in enumerate(['a', 'b', 'c']): print(i,value, end=', ') # usage of unpacking, enumerate returns tuple.
for t in enumerate(['a', 'b', 'c']): print(t, end=', ')
for t in enumerate(['a', 'b', 'c']): i,v = t; print(i, v, end=', ')

print('\n','-'*50)
t = (('code1', '1234'), ('code2', '2121')) # nested tuple
for name, (d1, d2, d3, d4) in t:
    print (name, d1,d2,d3,d4)

# ===============
# albums = [('Eminem', 2000, ['my mom', 'iam not afraid']),
#           ('Selena', 2010, ['heart', 'same old love', 'sad']),
#           ]# nested tuple

print(albums[1][2][2]) # sad, nested indexuing

for album  in albums :
    artist, year, songs = album
    print ('\n\n',artist, year, songs)
    for song in songs:
        print(song, end='|')

# list to tuple conversion
(a,b,c) = t  = ['aa', 'bb','cc']
print(t)
print(a,b,c,c)

#   tuple to list conversion
[a,b,c] = ('aa', 'bb','cc')
print(a,b,c,c)



