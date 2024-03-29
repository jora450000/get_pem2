FROM docker.io/ubuntu:20.04
COPY requirements.txt /

RUN apt-get -y update
RUN apt-get install python3 python3-pip -y && apt-get install python3-venv -y && apt-get install zip -y &&  apt-get install p7zip-full -y && apt-get install  unrar -y && apt install git -y

RUN  pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN git clone https://github.com/wummel/patool.git

EXPOSE 5000

CMD ["gunicorn", "--bind", ":5000",  "get_pem2:app"]
#ENTRYPOINT ["./gunicorn.sh"]
