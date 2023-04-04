FROM python:3.10
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y \
    freetds-bin \
    freetds-common \
    freetds-dev

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]