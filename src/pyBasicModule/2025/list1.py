# ==========================
# All Operations
# =========================

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
