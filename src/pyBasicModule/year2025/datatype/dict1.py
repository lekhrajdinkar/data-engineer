def dictDemo():
    # Create a dictionary
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }

    # 🔍 Accessing values
    print(person["name"])            # Alice
    print(person.get("age"))         # 30
    print(person.get("gender", "N/A"))  # Default if key doesn't exist

    # ✍️ Updating values
    person["age"] = 31

    # ➕ Adding new key-value pair
    person["job"] = "Engineer"

    # ❌ Deleting a key
    del person["city"]
    person.pop("job")

    # ✅ Check if key exists
    if "name" in person:
        print("Name exists")

    # 🔁 Loop through keys and values
    for key, value in person.items():
        print(f"{key}: {value}")

    # 🔑 Get only keys or values
    print(list(person.keys()))    # ['name', 'age']
    print(list(person.values()))  # ['Alice', 31]

    # 📦 Copy dictionary
    person_copy = person.copy()

    # 🔁 Merge dictionaries (Python 3.9+)
    extra = {"country": "USA"}
    person |= extra  # same as person.update(extra)

    # 🧹 Clear all entries
    # person.clear()

    # 🧾 Final result
    print("Final:", person)
