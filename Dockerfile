FROM python:3.9

COPY requirements.txt requirements.txt
COPY data/data.yaml data/data.yaml

RUN pip install -r requirements.txt