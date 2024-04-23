FROM python:3.9-slim

WORKDIR /flask-graphql

#RUN apt update && apt install build-dep python-psycopg2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0", "src:create_app()"]
