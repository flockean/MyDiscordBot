FROM python:3.12-slim
LABEL maintainer="lucas.buchholz1@gmail.com"
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y
RUN apt-get install -y ffmpeg git curl
COPY requirements.txt ./

RUN pip install -U pip
RUN pip install -r requirements.txt

WORKDIR /app
COPY ./src .

ENV DISCORD_BOT_HOST 0.0.0.0
ENV DISCORD_BOT_PORT 8000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:8000/live || exit 1

ENTRYPOINT ["python", "__main__.py"]