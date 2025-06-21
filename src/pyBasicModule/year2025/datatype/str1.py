def str_all():
    # --- 1. String Creation ---
    s1 = "hello"
    s2 = 'world'
    s3 = """multi-line
    string"""
    s4 = str(1234)         # From int
    s5 = str(['a', 'b'])    # From list
    print(f"➕", s1, s2,s3,s4,s5, type(s5))

    # --- 2. Deletion (via reassignment) ---
    s_del = "temporary"
    del s_del  # Now s_del is gone

    # --- 3. Update (strings are immutable) ---
    s_orig = "python"
    s_updated = s_orig[:2] + "X" + s_orig[3:]
    print("Updated:", s_updated)  # → 'pyXhon'

    # --- 4. Manipulation ---
    msg = "  Hello World!  "
    print(msg.lower())             # '  hello world!  '
    print(msg.strip())             # 'Hello World!'
    print(msg.replace("World", "Python"))  # '  Hello Python!  '
    print(msg.startswith("  He"))  # True
    print(msg.endswith("!  "))     # True
    print(msg.split())             # ['Hello', 'World!']
    print("-".join(["2025", "06", "20"]))  # '2025-06-20'

    # --- 5. Format / f-strings ---
    name = "Lekhraj"
    score = 95.1234
    print(f"{name.upper()} scored {score:.2f}")  # 'LEKHRAJ scored 95.12'

    # --- 6. Escape sequences ---
    path = "C:\\Users\\lekhraj"
    quote = "He said, \"Python is fun!\""

    # --- 7. Raw strings ---
    regex = r"\d{3}-\d{2}-\d{4}"  # No escaping needed

    # --- 8. Slicing, indexing ---
    s = "abcdefgh"
    print(s[1:5])         # 'bcde'
    print(s[::-1])        # 'hgfedcba' reverse string

    # --- 9. Performance (avoid += in loop) ---
    import time
    words = ["one", "two", "three"]
    start = time.time()
    result = "".join(words)  # Faster than +=
    end = time.time()
    print("Join performance:", end - start)

    # --- 10. Tricky: reversing words in sentence ---
    sentence = "The quick brown fox"
    reversed_words = " ".join(sentence.split()[::-1])  # 'fox brown quick The'
    print("Reversed:", reversed_words)

    # --- 11. Advanced: string translation ---
    trans_table = str.maketrans("aeiou", "12345")
    print("hello world".translate(trans_table))  # h2ll4 w4rld

    # --- 12. Use case: extract domain from email ---
    email = "user@example.com"
    domain = email.split("@")[1]
    print("Domain:", domain)

    # --- 13. Use case: clean log line ---
    log = "[ERROR]   Disk full   "
    clean = log.strip(" []").lower() # space. [, ] -> strip these 3. default takes only  space
    print("Cleaned:", clean)  # error   disk full

    # --- 14. Use case: count word frequency ---
    from collections import Counter
    words = "one one two three two two".split()
    counts = Counter(words)
    print(counts)  # {'one': 2, 'two': 3, 'three': 1}

    # --- 15. Use case: detect palindrome ---
    s = "madam"
    print(f"{s} is palindrome? {s == s[::-1]}")
