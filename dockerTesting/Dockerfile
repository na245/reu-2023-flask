FROM ubuntu:22.04
FROM python:3.8

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

WORKDIR /dockerTesting
COPY . .
RUN pip3 install -r requirements.txt

#COPY ./databaseUpdate . 
#COPY ./filePassing .

CMD ["python3","driver.py"]
#CMD python3 -m http.server 8000
