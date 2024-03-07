FROM python:3.11.5-slim

WORKDIR /

RUN mkdir ./log

RUN apt-get update && apt-get install -y curl vim
RUN apt-get clean

RUN pip install --upgrade pip

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"
COPY producer.py /
COPY consumer.py /
COPY pyproject.toml /
COPY poetry.lock /
RUN poetry install --no-dev
RUN yes | poetry cache clear . --all




