# py (3.10+)
## A. basic - Datatypes, etc
- everything is object , Dynamically typed (duck type), **object** (base class)
### 1. datatype
- ![img_2.png](99_IMG/001/img_2.png)
- inbuilt class, lower case unlike java, use module for more types.
- **type, class, Enum, module**
- range, int, float, complex(imaginary number), **decimal**.Decimal
- str (string, char), bool
- NoneType is type, None : A singleton object representing “no value” or “null” :point_left:
- **collection/s** - simpler inbuild + module:collections
    - **enumerate( list1 )** while looping need , Index + Value Together
    - **array.array or list []** 
      - Mutable, Mixed types allowed
      - array.array -> memory-efficient for large numeric data |  array.array('i', [1, 2, 3])  # 'i' means integer
      - students = [Student("Alice", 22, 88),Student("Bob", 20, 95)]; students[0] = Student("Charlie", 23, 70); mutate
      - students.sort(**key**=lambda s: s.grade, **reverse**=True/False)
      - [list1.py](../../src/pyBasicModule/2025/list1.py)
      - :point_right: .remove("item1"), pop(), l1 += l2,  sort(), reverse(), copy()
    - **tuple ()**
        - Immutable, hetro
        - fruits = ["apple", "banana", "cherry"]; fruits[0] = "orange"; :x:
    - **dict {}**
        - K:V pair, obj literal in js, alternative for Map, mutable
        - person = {"name": "Alice", "age": 30}
        - person["age"] === person.age
        - :point_right: .pop(k1) or del dict1[k1], dict1[k1] or dict1.get(k1,"defaultv1"), .items(), .keys(), .values(), .copy(), update(dict2) or dict1 |= dict2
        - [dict1.py](../../src/pyBasicModule/2025/dict1.py)
    - **set, frozenset([])** 
    - **bytes, bytearray, memoryview**
    - **generics with collection**
        - type hinted in 3.9+ ??
        - Optional with type hints ??
- **Special Python-only Types** : ??
  - **Ellipsis**
  - **NotImplemented**
  - **NamedTuple, dataclass** : Lightweight data containers
  
### 2. Sequence types

| Type         | Mutable | Ordered | Duplicates Allowed | Indexable |
| ------------ | ------- | ------- | ------------------ | --------- |
| `list`       | ✅ Yes   | ✅ Yes   | ✅ Yes              | ✅ Yes     |
| `tuple`      | ❌ No    | ✅ Yes   | ✅ Yes              | ✅ Yes     |
| `range`      | ❌ No    | ✅ Yes   | ✅ Yes              | ✅ Yes     |
| `str`        | ❌ No    | ✅ Yes   | ✅ Yes              | ✅ Yes     |
| `bytes`      | ❌ No    | ✅ Yes   | ✅ Yes              | ✅ Yes     |
| `bytearray`  | ✅ Yes   | ✅ Yes   | ✅ Yes              | ✅ Yes     |
| `memoryview` | ✅ Yes\* | ✅ Yes   | ✅ Yes              | ✅ Yes     |

- **operation on sequence**
  - ??
  - sum(), max(), any()
  
### 3. prog constructs
- **logical Operator** : and or not
- **bitwise** : or ` | and & | not ~ | XOR ^ | << | >>
- **Identity and Membership Operators**

  | Operator | Description     | Example      | Result       |
  | -------- | --------------- | ------------ | ------------ |
  | `is`     | Same object     | `a is b`     | `True/False` |
  | `is not` | Not same object | `a is not b` | `True/False` |
  | `in`     | Exists in     | `'a' in 'cat'`     | `True` |
  | `not in` | Not exists in | `'z' not in 'cat'` | `True` |

- if, elif, else
- **Ternary** : a if condition else b
- **loops**: 
    - for i in range(3) / [1, 2, 3] / {1, 2, 3} 
    - while x > 0: 
    - break | continue 
    - warp with enumerate(list1)
    - **itertools** Powerful Looping Utilities
      - for i in itertools.`repeat`(5, 3):
      - for i in itertools.`cycle`([1, 2]):
      - ...
    - for key, val in **dict1**.items():
    - List/set comprehension + generator expression
- **util**: print(), hash(), len(), dir(module1) ??
- yeild ??
- async for or yield from ??
  
### 4. modules
- .py files
- import module : no need to explicitly export like in TS
- python3 **-m** module1.py : ??
- common built-in modules :  os,  sys,  datetime,  json,  random,  re,  math
- print(**dir**(math_ops))  # Lists all functions, classes, etc.  <<<
- Check if module is run directly => if __name__ == "__main__": \ print("Running math_utils directly")
- installing 3rd-party modules using pip3
- 2 ways to run a module =>  python3 math_utils.py + import math_utils

### 5. special method
- If want a custom class to act like a list/dict/etc., implement special methods :point_left:
- [02_specialClass.py](../../src/pyBasicModule/2025/style_oops/02_specialClass.py)
```
__getitem__(self, index)  | a[1]
__setitem__(self, index)  | a[1] = 123
__delitem__(self, index)  | del a[1] 
__iter__(self)  | for x in obj1:  ,return some collection 
__len__(self) | len a
__contains__(self,item) | item1 in obj1
__add__(self, other) | obj1 + other1
__eq__ (self, other) |  obj1 == other1
__repr__(self) | print(obj1)
__str__(self) | str(obj)
__format__(self) | format(obj1)
__bytes__(self) | bytes(obj1)
...
...
```

- a and b are objects, check below:

| Method   | Operation | Example  |
| -------- | --------- | -------- |
| `__eq__` | `==`      | `a == b` |
| `__ne__` | `!=`      | `a != b` |
| `__lt__` | `<`       | `a < b`  |
| `__le__` | `<=`      | `a <= b` |
| `__gt__` | `>`       | `a > b`  |
| `__ge__` | `>=`      | `a >= b` |

| Method         | Operation  | Example  |
| -------------- | ---------- | -------- |
| `__add__`      | `+`        | `a + b`  |
| `__sub__`      | `-`        | `a - b`  |
| `__mul__`      | `*`        | `a * b`  |
| `__truediv__`  | `/`        | `a / b`  |
| `__floordiv__` | `//`       | `a // b` |
| `__mod__`      | `%`        | `a % b`  |
| `__pow__`      | `**`       | `a ** b` |
| `__neg__`      | Unary `-a` |          |

| Method         | Purpose          | Example      |
| -------------- | ---------------- | ------------ |
| `__getitem__`  | Index access     | `obj[0]`     |
| `__setitem__`  | Index assignment | `obj[0] = x` |
| `__delitem__`  | Delete item      | `del obj[0]` |
| `__len__`      | Length           | `len(obj)`   |
| `__contains__` | Membership check | `x in obj`   |

| Method      | Purpose              | Example     |
| ----------- | -------------------- | ----------- |
| `__call__`  | Make object callable | `obj()`     |
| `__enter__` | Context start        | `with obj:` |
| `__exit__`  | Context end          |             |

| Method     | Purpose           | Example     |
| ---------- | ----------------- | ----------- |
| `__hash__` | Hash for dict/set | `hash(obj)` |
| `__bool__` | Truth value       | `if obj:`   |

### 6. imports / export
- import modules prg:
```text
my_app/
│
├── utils/
│   ├── __init__.py
│   ├── math_ops.py
│   └── string_ops.py
├── main.py

---
from . import math_ops           # same package, or shorthand --> import math_ops
from ..utils import string_ops   # parent package
from utils import math_ops
from utils.math_ops import add
---
# == math_ops.py ==
def add(a, b):
    return a + b

print("This runs always")  # Runs always

if __name__ == "__main__":
    print("Running directly!")  # Runs only when this file is run directly
```

---
## B. Tips
### Tip-1
- `*args` → captures extra positional arguments as a **tuple**
- `**kwargs` → captures extra keyword arguments as a **dict**
- `__name__`
    - special built-in variable in every Python file (module-1.py)
    - `__main__`: if module ran directly
    - `module-1` : if module ran by being imported

### Tip-2 generator Expression vs Comprehension
- **Comprehensions**. eg:
    - even_set_squares = [x*x for x in range(10) if x % 2 == 0] # List comprehension
    - even_set = {x for x in range(10) if x % 2 == 0} # set comprehension
    - Eager Evaluation: Evaluates all items immediately.
    - Stores all values in memory as a full list.
- **generator expression** 
    - like a list comprehension but produces items one at a time using lazy evaluation
    - saves memory, consume less, and is faster for large data
    - syntax: (expression for item in iterable if condition)
    - (x*x for x in range(10) if x % 2 == 0)

| Use Case                | Generator | List |
| ----------------------- | --------- | ---- |
| Large datasets          | ✅         | ❌    |
| One-time iteration      | ✅         | ❌    |
| Need all values at once | ❌         | ✅    |
| Memory critical apps    | ✅         | ❌    |

### Tip-3
- Iteration/Streams vs Comprehensions ??
- Mutability or performance comparison ??
- **decorator** ??

---
## C. Programing style
### C.1. Procedural
### C.2. OOPS
- A **package** is a directory containing an `__init__.py`
- **enum.Enum**
- **classes**
    -  constructor: `def __init__(self):`
    - no getters/setters, can access attributes directly
    - weak : private/protected/public : __ , _ ,  --> not enforced, Name mangling only
    - **instance variable** with self.xxxx
    - **static variable** -> var without self + `@staticmethod`
    - `@classmethod` ??
    - create object without **new operator**, unlike java
    - `obj.__class__` -> Reference to class
- **Abstraction** : abstract class using **abc module**
    - no native interface
    - module:ABC + @abstractmethod
- **Polymorphism** 
    - only **overriding** happens, since duck typing.
    - **overloading**  (no native support)
      - achieve same with *args, **kwargs ( to dict)
      - with `@singledispatch` [02_oops.py | section-2](../../src/pyBasicModule/2025/style_oops/02_oops.py)
      - fact: last defined method with the same name overrides previous ones
- **error handling**: 
    - try, except MyError as e, finally

### C.3 functional

| Type                          | Description          | Example         |
| ----------------------------- | -------------------- | --------------- |
| `function`                    | Function object      | `def f(): pass` |
| `lambda`                      | Anonymous function   | `lambda x: x*2` |
| `generator`                   | Lazy sequence        | `yield`         |
| `coroutine`                   | For async/await      | `async def`     |
| `classmethod`, `staticmethod` | Class/static methods |                 |

- **functional Operation**
    - filter, map, any, all, sum ??

---
## D. module (ext)
### 1. commonly used ??
- math, cmath, decimal
- collections
- datetime, timedelta
- BaseException, Exception
- function, lambda, callable
- threading, asyncio, concurrent
- open, io, os, pathlib

### 2. collections ??
- Thread-safe collections
- generics
- collections.deque
- queue.Queue, deque, heapq

### 3. fastapi + httpx  ??
- uvicorn src.main:etlapp --reload
- real-world APIs.
- NumPy, Pandas, or parallel loops

## E. profile / performance ??
- python -m timeit -s "lst = list(range(1000))" "sum(lst)"
- python -m cProfile your_script.py

## Z. more
- Design patterns (Java vs Python) ??
- 
