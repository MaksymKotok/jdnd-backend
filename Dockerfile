FROM python:3.12.3-alpine

WORKDIR /code

COPY ./req.txt /code/req.txt

RUN pip install --no-cache-dir -r req.txt

COPY . /code/