FROM alpine:3.18

#################################
# Set environment variables
#################################
ARG HADOOP_AWS_VERSION=3.3.4
ARG AWS_SDK_VERSION=1.12.262

ENV PYSPARK_HADOOP_VERSION=3
ENV SPARK_LOCAL_IP=127.0.0.1
ENV PYSPARK_PYTHON=python3

ENV PYTHONPATH="/usr/lib/python3.11"
ENV SPARK_HOME="${PYTHONPATH}/site-packages:/pyspark"
ENV HADOOP_HOME="${SPARK_HOME}/jars"
ENV CLASSPATH="${SPARK_HOME}/jars:${SPARK_HOME}/jars/hadoop-aws-${HADOOP_AWS_VERSION}.jar:${SPARK_HOME}/jars/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar:${CLASSPATH}"

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
# Set Java options for Spark
ENV _JAVA_OPTIONS="-Xmx24g"

#################################
# install
#################################
# Python
RUN apk add --no-cache python3 \
    && python3 -m ensurepip \
    && apk add python3-dev \
    && rm -rf /usr/lib/python*/ensurepip \
    && if [[ ! -e /usr/bin/pip ]]; then ln -s pip3 /usr/bin/pip; fi \
    && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

# pip
RUN pip install  --upgrade pip setuptools

# kafka
RUN apk add  --upgrade librdkafka-dev

# devtool
RUN apk update && apk upgrade \
    && apk add --update tzdata curl sudo unzip wget git bash grep coreutils nss gcc libc-dev g++ \
    && rm -rf /var/cache/apk/*

# java
RUN apk update && apk upgrade \
    #&& apk add ca-certificates  && upgrade-ca-certificates \
    && apk add --no-cache openjdk17 --repository=https://dl-cdn.alpinelinux.org/alpine/v3.17/community \
    && rm -rf /var/cache/apk/*

# panda
RUN apk update && apk upgrade \
    && apk add --no-cache py3-pandas \
    && rm -rf /var/cache/apk/*

RUN rm  -r /root/.cache

COPY requirements.txt .
RUN pip install -r requirements.txt


#####################################
# Set up : hadoop. hadoop-aws, spark
#####################################
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_AWS_VERSION}/hadoop-aws-${HADOOP_AWS_VERSION}.jar

RUN wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar

#RUN echo spark.hadoop.fs.s3a.aws.credential.provider=com.amazonaws.auth.DefaultAWSCredentialsProviderChain
RUN echo spark.hadoop.fs.s3a.aws.credential.provider=com.amazonaws.auth.EC2ConatinerCredentialsproviderWrapper


EXPOSE 80
ADD ./ .

RUN chmod +x ./app_etl_run.sh

ENTRYPOINT ["app_run.sh"]
CMD ["etl-1"]


