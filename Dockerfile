FROM python:3.9

MAINTAINER Runze Wu

ENV PYTHONUNBUFFERED 1

#RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
#&& apt-get clean  \
#    && apt-get update  \
#    && apt-get install python3-dev default-libmysqlclient-dev -y

RUN mkdir -p /var/code
WORKDIR /var/code

ADD requirements.txt /var/code
ADD backend/ /var/code

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD echo "--------end----------"
