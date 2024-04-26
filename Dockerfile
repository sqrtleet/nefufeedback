FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /test
COPY requirements.txt /test
RUN python3 -m pip install -r requirements.txt

COPY . /test

CMD python3 main.py