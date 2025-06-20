# cd .\src\pyBasicModule\year2025\ 🏃‍♂️
# python -m main2025
# root path: C:\Users\Manisha\Documents\GitHub\idea\02-etl-pyspark\src\pyBasicModule\year2025\

from datatype import main as datatype_main
#import datatype

if (__name__ == "__main__"):
    datatype_main.typeDemo()
    datatype_main.printCurrentModule()
    datatype_main.printOtherModule_static()
    datatype_main.printOtherModule_dynamic("datatype.sequence03")