FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y inotify-tools

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0", "src:create_app()"]
