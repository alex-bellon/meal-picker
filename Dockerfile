FROM ubuntu:18.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev
RUN apt-get install -y python3 python3-pip

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

ARG USER
ENV USER $USER

COPY ./server.py /server.py
COPY ./mealpicker.py /mealpicker.py
COPY ./meals.json /meals.json
COPY ./templates /templates
COPY ./static /static

RUN useradd -m $USER

EXPOSE 9000

RUN export FLASK_APP=server

CMD ["python3", "server.py"]
