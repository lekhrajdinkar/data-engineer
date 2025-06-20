# Type Conversion
x = "123"
y = int(x)          # string to int
z = float(y)        # int to float
s = str(z)          # float to string
b = bool(s)         # non-empty string to True

print(y, type(y))   # 123 <class 'int'>
print(z, type(z))   # 123.0 <class 'float'>
print(s, type(s))   # '123.0' <class 'str'>
print(b, type(b))   # True <class 'bool'>

# List & Set
t = (1, 2, 3)
l = list(t)         # tuple to list
s = set(l)          # list to set

print(l, type(l))   # [1, 2, 3] <class 'list'>
print(s, type(s))   # {1, 2, 3} <class 'set'>

# Type Checking
print(isinstance(l, list))   # True
print(isinstance(s, dict))   # False
print(type(10) == int)       # True
