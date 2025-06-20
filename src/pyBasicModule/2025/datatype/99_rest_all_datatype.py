# ==== section-1 : type

print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type('hello'))   # <class 'str'>
print(type([1, 2]))    # <class 'list'>
print(type({'a': 1}))  # <class 'dict'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>

# ==== section-1 : datatype Conversion - using call const, easy

int(3.14)      # 3
float(5)       # 5.0
str(100)       # '100'
list('hello')  # ['h', 'e', 'l', 'l', 'o']
tuple([1,2,3]) # (1, 2, 3)
set([1,2,2,3]) # {1, 2, 3}