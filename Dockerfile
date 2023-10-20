ARG PYTHON_VERSION="3.10"
FROM python:${PYTHON_VERSION}

ARG PIP_ARG=" "

ENV PYTHONDONTWRITEBYTECODE='x' \
    PYTHONUNBUFFERED='x'

WORKDIR /cowptain

COPY linters.txt ./linters.txt
COPY servers.txt ./servers.txt

RUN pip install -r linters.txt -r servers.txt

COPY Makefile ./Makefile
COPY pyproject.toml .
COPY wsgi ./wsgi
COPY unit ./unit
COPY src ./src

RUN pip install ${PIP_ARG} .
