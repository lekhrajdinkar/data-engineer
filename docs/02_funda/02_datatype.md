 - https://chat.deepseek.com/a/chat/s/1989e256-eb5f-4b3b-95b6-cbf76bf1bf5b
 - [001_datatypes](../000_py_learn/001_datatypes)
---
## A Data Types
![img_2.png](99_IMG/001/img_2.png)

### 1 Numeric : int, float, complex
```python
# integer
x = 10
y = -5

# float
a = 3.14
b = -0.001
c = 2.5e2  # 250.0

# Numbers with real and imaginary parts (j or J suffix).
d = 3 + 4j
e = 2 - 1j
f = complex(1, 2)  # 1+2j
```
### 2 Sequence Types : string, list,set,tuple
```python
# String
s1 = 'Hello'
s3 = '''Multi-line
string'''
s4 = """Another multi-line
string"""

# Immutable sequence of bytes (0-255).
b = b'hello'
# b[0] = 72  # Error - immutable

# list
list = [1, 2.5, 'three', True]
list[0] = 10  # mutable

st = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
st.add(5)
fst = frozenset([1, 2, 3, 3])  # Immutable version of set.

# Ordered, immutable sequence of elements 
# can be mixed types
tuple = (1, 2.5, 'three', False)
```
---
### 3 Mapping Type
```python
# Dictionary 
dct = {'name': 'Alice', 'age': 25, 'city': 'New York'}
dct['age'] = 26  # mutable
```
---
### 4 more : boolean, byte, byteArray, None
```python
# Immutable sequence of bytes (0-255).
b = b'hello' # b[0] = 72  # Error - immutable
empty = None # Represents absence of a value.
del b # delete a single object or multiple objects

```
---
## B Checking Data Types
```python
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type('hello'))   # <class 'str'>
print(type([1, 2]))    # <class 'list'>
print(type({'a': 1}))  # <class 'dict'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
```

---
## C Type Conversion
```python
int(3.14)      # 3
float(5)       # 5.0
str(100)       # '100'
list('hello')  # ['h', 'e', 'l', 'l', 'o']
tuple([1,2,3]) # (1, 2, 3)
set([1,2,2,3]) # {1, 2, 3}
```

---
## D more
### 1. reserved keyword
```
and	as	assert
break	class	continue
def	del	elif
else	except	False
finally	for	from
global	if	import
in	is	lambda
None	nonlocal	not
or	pass	raise
return	True	try
while	with	yield
```
