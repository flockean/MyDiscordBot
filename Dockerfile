FROM python:3.12-slim
LABEL maintainer="lucas.buchholz1@gmail.com"
COPY requirements.txt ./

RUN pip install -U pip
RUN pip install -r requirements.txt

WORKDIR /app
COPY main.py ./
COPY ./src ./src


ENTRYPOINT ["python3", "main.py"]