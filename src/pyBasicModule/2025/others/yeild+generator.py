"""
- yeild
  - yield returns a value without exiting the function.
  - the function’s state is saved between calls.
  - It produces a generator object.
"""
# ======= creator generator (stream-1)
def count_up_to(n):
    i = 1
    while i <= n:
        yield i # pause here, next() will resume
        i += 1

gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) → raises StopIteration

# ======= creator generator (stream-2 file)

def read_lines(file_path):
    with open(file_path) as f: # returns TextIOWrapper
        for line in f:
            yield line.strip()

for line in read_lines("log.txt"):
    print(line)


# ======== Looping Through a Generator

for x in count_up_to(3):
    print(x)  # 1, 2, 3

