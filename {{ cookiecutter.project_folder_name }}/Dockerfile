FROM python:3.10
LABEL maintainer="Francisco Schulz"

WORKDIR /src

RUN pip install --upgrade pip && \
    pip install poetry

COPY poetry.lock pyproject.toml .

RUN poetry install

COPY ./src .
