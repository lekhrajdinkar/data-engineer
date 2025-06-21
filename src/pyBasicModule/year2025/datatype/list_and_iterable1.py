# ==========================
# All Operations
# =========================

def listDemo():
    # 📄 Create a list
    fruits = ["apple", "banana", "cherry"]

    # 🔍 Access items
    print(fruits[0])        # apple
    print(fruits[-1])       # cherry
    print(fruits[1:])       # ['banana', 'cherry']

    # ✍️ Update an item
    fruits[1] = "blueberry"

    # ➕ Add items
    fruits.append("date")               # Add to end
    fruits.insert(1, "kiwi")            # Insert at index

    # ➖ Remove items
    fruits.remove("apple")              # Remove by value
    last = fruits.pop()                 # Remove last item
    del fruits[0]                       # Delete by index

    # 🔁 Loop over list
    for fruit in fruits:
        print(fruit)

    # 📦 Combine lists
    more_fruits = ["mango", "pear"]
    fruits += more_fruits               # Extend list

    # 🧹 Clear list
    # fruits.clear()

    # ✅ Check existence
    if "mango" in fruits:
        print("Mango is here!")

    # 🔄 Sort and reverse
    fruits.sort()
    fruits.reverse()

    # 🧾 Length and copy
    print(len(fruits))                 # Number of items
    copy_list = fruits.copy()

    # 🔁 List comprehension
    lengths = [len(f) for f in fruits]

    # 🧾 Final output
    print("Final fruits:", fruits)
    print("Lengths:", lengths)

    # ============= Section-2 : zip

    names = ["Alice", "Bob"]
    ages = [25, 30]
    for name, age in zip(names, ages):
        print(name, age)

    # ============= Section-3 :  enumerate

    items = ['a', 'b', 'c']
    for index, value in enumerate(items):
        print(index, value)

    # ============= Section-4 :  itertools — Powerful Looping Utilities

    from itertools import product
    for x in product([1, 2], ['a', 'b']):
        print(x)
    # (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')

    # ======== Section -5  Loop tips

    ## 1 Use Built-in Functions Instead of Manual Loops
    my_list = [1,2,3,4,5,6]
    # ✅ Fast
    total = sum(my_list)

    # ❌ Slower
    total = 0
    for x in my_list:
        total += x

    ## 2 Use List Comprehensions Instead of for Loops
    # ✅ Fast
    squares = [x * x for x in range(1000)]

    # ❌ Slower
    squares = []
    for x in range(1000):
        squares.append(x * x)

    ## 3 Avoid Repeated Computation in Loop
    # ✅ Good
    length = len(my_list)
    for i in range(length):
        pass

    # ❌ Bad
    for i in range(len(my_list)):
        pass

    ## 4 Use enumerate() and zip() Instead of Manual Indexing

    ## 5 Saves memory by not storing the full list in RAM
    # ✅ Better for big data
    total = sum(x * x for x in range(1000000)) # Generator expression
    # ❌ List comprehension stores all
    total = sum([x * x for x in range(1000000)])


def comprehension_demo():
    squrare = [x*x for x in range(10) if x % 2 == 0]
    # List comprehension : fast + consume memory
    # <class 'list'>
    print(f"comprehension :: [x*x for x in range(10) if x % 2 == 0]", squrare, type(squrare))


def generation_demo():
    #<generator object generation_demo.<locals>.<genexpr> at 0x0000022B6A09C450> <class 'generator'>
    square_gen = (x * x for x in range(10) if x % 2 == 0)  # Generator expression
    print("generator :: (x*x for x in range(10) if x % 2 == 0)", square_gen, type(square_gen))
    for item in square_gen:
        print(item, type(item), f"ℹ️")





