FROM python:3.7-alpine

RUN apk update && apk upgrade 
RUN apk add --no-cache openssl-dev libffi-dev musl-dev gcc

RUN pip install --no-cache-dir notion python-telegram-bot
RUN mkdir /src

WORKDIR /src

CMD python /src/bot.py
