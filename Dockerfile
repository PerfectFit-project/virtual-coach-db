FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install wheel

ADD requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Use dbschema as working directory, because we want alembic to be used from there
WORKDIR /app/dbschema
