FROM python:3.8-slim-buster
 
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /EvaMaria
WORKDIR /EvaMaria
COPY . .
COPY start.sh  .
CMD ["python3", "bot.py"]
