# Copyright (c) IIIedu BDSE.
ARG BASE_CONTAINER=jupyter/pyspark-notebook
FROM $BASE_CONTAINER

LABEL maintainer="BDSE12 Project <contactus@iii.org.tw>"
LABEL maintainer="指導老師：楊禎文老師"

COPY module module 
COPY jar jar 
COPY sample sample 
COPY lab  lab

USER root
RUN cp -r ~/module/sparkxgb /opt/conda/lib/python3.7/site-packages #xgboost會用的模組
RUN cp -r ~/module/mmlspark /opt/conda/lib/python3.7/site-packages #lightgbm會用的模組
RUN cp ~/jar/*.jar /usr/local/spark/jars  #最重要的jar檔
RUN mv ~/lab/*  /usr/local/bin/    #如果要使用notebook 就把這行註解，刪掉image重新跑一次程式就可以
RUN rm -r ~/module
RUN rm -r ~/jar
RUN rm -r ~/lab
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
USER jovyan


