# ========== Sequence operation ===========
# python -m src.pyBasicModule.2025.datatype.sequence03 🏃🏃‍♀️🏃‍♂️ RUN

# List operations
lst = [10, 20, 30, 40, 50]
print(lst[2])              # Indexing → 30
print(lst[1:4])            # Slicing → [20, 30, 40]
print(len(lst))            # Length → 5
print(20 in lst)           # Membership → True
print(lst + [60])          # Concatenation → [10, 20, 30, 40, 50, 60]
print(lst * 2)             # Repetition → [10, 20, ..., 50, 10, 20, ..., 50]
print(min(lst), max(lst))  # Min/Max → 10 50
print(sum(lst))            # Sum → 150
print(lst.index(30))       # Index of 30 → 2
print(lst.count(10))       # Count → 1
print(sorted(lst))         # Sorted → [10, 20, 30, 40, 50]
print(list(reversed(lst))) # Reversed → [50, 40, 30, 20, 10]

# String operations
s = "hello world"
print(s[4])                 # 'o'
print(s[0:5])               # 'hello'
print(len(s))               # 11
print('world' in s)         # True
print(s + "!")              # 'hello world!'
print(s * 2)                # 'hello worldhello world'
print(min(s), max(s))       # ' ' 'w'
print(s.index('o'))         # 4
print(s.count('l'))         # 3
print(sorted(s))            # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(''.join(reversed(s))) # 'dlrow olleh'

s = "python"
print(s[-1])   # 'n'
print(s[-2])   # 'o'
print(s[-6])   # 'p'
print(s[-3:])   # gets last 3 elements


