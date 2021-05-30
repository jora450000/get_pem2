FROM ubuntu:20.04
COPY requirements.txt /

RUN apt-get -y update
RUN apt-get install python3 python3-pip -y

RUN apt-get install python3-venv -y
RUN apt-get install zip -y 
RUN apt-get install p7zip-full -y
RUN apt-get install  unrar -y

RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000

CMD ["gunicorn", "--bind", ":5000",  "get_pem2:app"]
#ENTRYPOINT ["./gunicorn.sh"]