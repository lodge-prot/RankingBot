FROM python:3.7
USER root

WORKDIR /root/rankingbot
RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV PYTHONUNBUFFERD 1

RUN apt-get install -y vim less tree
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY ./requirements.txt /root/rankingbot
COPY ./.dotfiles/.bashrc /root/.bashrc
RUN pip install -r requirements.txt

#EXPOSE 80
#EXPOSE 443
