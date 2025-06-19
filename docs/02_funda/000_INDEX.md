- py 2: [https://chatgpt.com/c/68536dbf-dd20-800d-9328-f38fcbdef71e](https://chatgpt.com/c/68536dbf-dd20-800d-9328-f38fcbdef71e)
- py 1: [https://chatgpt.com/c/68535fab-0494-800d-af09-a35817d88f6a](https://chatgpt.com/c/68535fab-0494-800d-af09-a35817d88f6a)

---
# py (3.10+)
## A. basic - Datatypes, etc
- everything is object , Dynamically typed (duck type), **object** (base class)
### 1. datatype
- inbuilt class, lower case unlike java, use module for more types.
- **type, class, Enum, module**
- range, int, float, complex(imaginary number), **decimal**.Decimal
- str (string, char), bool
- NoneType is type, None : A singleton object representing “no value” or “null” :point_left:
- **collection/s** - simpler inbuild + module:collections
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
  
### 2. Sequence

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
  
### 3. prog constructs
- if, elif, else
- for i in range(3):
- while x > 0:
- in
- comparison ?? -> is , is not == !=
- util: print(), hash(), len(), ??
  
### 4. modules
- .py files
- import module : no need to explicitly export like in TS
- python3 **-m** module1.py : ??
- common built-in modules :  os,  sys,  datetime,  json,  random,  re,  math
- print(**dir**(math_ops))  # Lists all functions, classes, etc.  <<<
- Check if module is run directly => if __name__ == "__main__": \ print("Running math_utils directly")
- installing 3rd-party modules using pip3
- 2 ways to run a module =>  python3 math_utils.py + import math_utils

### special method
- If want a custom class to act like a list/dict/etc., implement special methods :point_left:
- [02_specialClass.py](../../src/pyBasicModule/2025/02_specialClass.py)
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
## B. tips
- print( *vargs)
- *vargs , **kwargs
- __name__
  - special built-in variable in every Python file (module-1.py)
  - `__main__`: if module ran directly
  - `module-1` : if module ran by being imported
- **Comprehensions**
  - squares = [x*x for x in range(5)] # List comprehension
  - even_set = {x for x in range(10) if x % 2 == 0} # set comprehension
- Iteration/Streams vs Comprehensions ??
- Mutability or performance comparison ??
- `*args` → captures extra positional arguments as a **tuple**
- `**kwargs` → captures extra keyword arguments as a **dict**
- decorator ??
---
## C. programing style
### C.1 procedural

### C.2 oops
- A **package** is a directory containing an __init__.py
- **enum.Enum**
- **classes**
    -  def __init__(self):
    - no getters/setters, can access attributes directly
    - weak : private/protected/public : __ , _ ,  --> not enforced, Name mangling only
    - **instance variable** with self.xxxx
    - **static variable** -> without self + `@staticmethod`
    - `@classmethod` ??
    - create object without **new operator**, unlike java
    - `obj.__class__` -> Reference to class
- **Abstraction** : abstract class using `abc module`
    - no native interface
    - module:ABC + @abstractmethod
- **Polymorphism** 
    - only **overriding** happens, since duck typing.
    - **overloading**  (no native support)
      - achieve same with *args, **kwargs ( to dict)
      - with `@singledispatch` [02_oops.py | section-2](../../src/pyBasicModule/2025/02_oops.py)
      - fact: last defined method with the same name overrides previous ones
- **special method**
    - sfdsf

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

### 2. collections
- Thread-safe collections
- generics
- collections.deque
- queue.Queue, deque, heapq

### 3. fastapi + httpx 
- uvicorn src.main:etlapp --reload
- real-world APIs.

## Z. more
- Design patterns (Java vs Python) ??
