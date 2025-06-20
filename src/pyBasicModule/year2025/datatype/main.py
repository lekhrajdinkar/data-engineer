def printCurrentModule():
    from . import main as me
    print("="*5, me.__name__, "="*5)
    #print("Name     :", me.__name__)
    print("Package  :", me.__package__)
    # print("Path     :", src.pyBasicModule.year2025.datatype.__path__)     # ✅ Only packages have this
    print("File     :", me.__file__)
    print("Doc      :", me.__doc__)

def printOtherModule_static():
    import src.pyBasicModule.year2025.datatype.sequence03 as seq
    print("="*5, seq.__name__, "="*5)
    #print("Name     :", seq.__name__)
    print("Package  :", seq.__package__)
    # print("Path     :", src.pyBasicModule.year2025.datatype.__path__)     # ✅ Only packages have this
    print("File     :", seq.__file__)
    print("Doc      :", seq.__doc__)

if (__name__ == "__main__"):
    printCurrentModule()
    printOtherModule_static()