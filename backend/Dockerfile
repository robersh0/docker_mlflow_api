FROM python:3.8

WORKDIR /app

EXPOSE 8000

RUN pip install pip --upgrade

RUN apt-get update && curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install nodejs && \
    npm i -g nodemon

ADD ./backend/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD ./backend/setup.cfg /app/setup.cfg
ADD ./backend/src /app/src