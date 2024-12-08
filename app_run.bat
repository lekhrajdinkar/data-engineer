set JAVA_HOME=C:\Program Files\Java\jdk-17
set PATH=%JAVA_HOME%\bin;%PATH%

set SPARK_HOME=C:\Users\Manisha\Documents\spark-3.5.3-bin-hadoop3
set PATH=%SPARK_HOME%\bin;%PATH%

set HADOOP_HOME=C:\Users\Manisha\Documents\winutils-master\hadoop-3.0.0
set PATH=%HADOOP_HOME%\bin;%PATH%
set HADOOP_CONF_DIR=$HADOOP_HOME\etc\hadoop



@echo off
REM Check if the argument is provided
if "%~1"=="" (
    echo Usage: %~nx0 ^<etl-name^>
    echo Example: %~nx0 etl-1 or etl-2
    exit /b 1
)

SET ETL=%~1

REM Run the main.py script with the ETL parameter
REM python src\main.py %ETL%

REM Uvicorn to look for the app object inside main.py
uvicorn src.main:etlapp --reload

pause
