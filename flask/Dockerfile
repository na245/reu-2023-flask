FROM ubuntu:22.04
FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

#CMD ["python", "app.py"]
CMD python app.py
