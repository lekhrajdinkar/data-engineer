# References
- [chatgpt - setup Dockerfile](https://chatgpt.com/c/674f855d-41b4-800d-a76f-39b5e7bff18c)
- [chatgpt - theory](https://chatgpt.com/c/67548d97-6268-800d-a8af-b8ccf576e5f0)
- [chatgpt - theory](https://chatgpt.com/c/6754cff4-b63c-800d-9e2f-caba7735697e)
- [chatgpt - project](https://chatgpt.com/c/67554038-a4d4-800d-a0aa-d51f621943a5)
- [chatgpt - trandformation and action on df](https://chatgpt.com/c/67578727-cefc-800d-9b0d-20eee5402296)
- [readme.md](readme.md) :point_left:
---

# install 
- **Python**:
  - 3.9.6 
  - 3.12

- **Java 17**: 
  - not higher.
  - else, java.lang.UnsupportedOperationException: **getSubject** is supported only if a security manager is allowed.
```
    # check java installtion dir
    /usr/libexec/java_home -V
    
    Matching Java Virtual Machines (2):
        23.0.1 (x86_64) "Oracle Corporation" - "OpenJDK 23.0.1" /Users/lekhrajdinkar/Library/Java/JavaVirtualMachines/openjdk-23.0.1/Contents/Home
        17.0.10 (x86_64) "Oracle Corporation" - "Java SE 17.0.10" /Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
    
    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
    export PATH=$JAVA_HOME/bin:$PATH
```

- **Spark**: 
  - https://www.apache.org/dyn/closer.lua/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz
    ```
    export SPARK_HOME=/Users/lekhrajdinkar/Documents/spark-3.5.3-bin-hadoop3
    export PATH=$SPARK_HOME/bin:$PATH
    ```
- **hadoop**:
  - https://github.com/steveloughran/winutils ( for windows only )
  
```
    === MAC : spark-3.5.3-bin-hadoop3  spark and hadoop , same ===
    
    export HADOOP_HOME=Users/lekhrajdinkar/Documents/spark-3.5.3-bin-hadoop3
    export PATH=$HADOOP_HOME/bin:$PATH
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    
    === windows : winutils ===
    
    set HADOOP_HOME=C:\Users\Manisha\Documents\winutils-master\hadoop-3.0.0
    set PATH=%HADOOP_HOME%\bin;%PATH%
    set HADOOP_CONF_DIR=$HADOOP_HOME\etc\hadoop
```
---
# start spark session
## spark-shell
```
spark-shell

Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/12/07 13:01:02 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://192.168.0.255:4040
Spark context available as 'sc' (master = local[*], app id = local-1733605263311).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.3
      /_/
         
Using Scala version 2.12.18 (Java HotSpot(TM) 64-Bit Server VM, Java 17.0.10)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 
```

## pyspark
- **pip install pyspark**
- pyspark 
- pyspark --master local[*]

```
pyspark --master local[*]

Python 3.9.6 (default, Feb  3 2024, 15:58:28) 
[Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/12/07 13:03:15 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
24/12/07 13:03:16 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.3
      /_/

Using Python version 3.9.6 (default, Feb  3 2024 15:58:28)
Spark context Web UI available at http://192.168.0.255:4041
Spark context available as 'sc' (master = local[*], app id = local-1733605396364).
SparkSession available as 'spark'.
```
