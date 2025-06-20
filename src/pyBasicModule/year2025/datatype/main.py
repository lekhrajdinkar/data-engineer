import importlib

def printCurrentModule():
    from . import main as me
    print("="*5, me.__name__, "="*5)
    #print("Name     :", me.__name__)
    print("Package  :", me.__package__)
    # print("Path     :", src.pyBasicModule.year2025.datatype.__path__)     # ✅ Only packages have this
    print("File     :", me.__file__)
    print("Doc      :", me.__doc__)

def printOtherModule_static():
    import src.pyBasicModule.year2025.datatype.sequence03 as seq # hardcoded modulename
    print("="*5, 'STATIC',  seq.__name__, "="*5)
    print("Package  :", seq.__package__)
    print("File     :", seq.__file__)
    print("Doc      :", seq.__doc__)

def printOtherModule_dynamic(mName: str):
    m1 = importlib.import_module(mName);
    print("="*5, 'DYNAMIC', m1.__name__, "="*5)
    print("Package  :", m1.__package__)
    print("File     :", m1.__file__)
    print("Doc      :", m1.__doc__)

def typeDemo():
    print(type(10))        # <class 'int'>
    print(type(3.14))      # <class 'float'>
    print(type('hello'))   # <class 'str'>
    print(type([1, 2]))    # <class 'list'>
    print(type({'a': 1}))  # <class 'dict'>
    print(type(True))      # <class 'bool'>
    print(type(None))      # <class 'NoneType'>

if (__name__ == "__main__"):
    typeDemo()
    printCurrentModule()
    printOtherModule_static()
    printOtherModule_dynamic("src.pyBasicModule.year2025.datatype.sequence03")