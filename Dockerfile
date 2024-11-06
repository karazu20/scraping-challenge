# syntax=docker/dockerfile:1
FROM selenium/standalone-chrome-112.0-chromedriver-112.0 
FROM python:3.10


WORKDIR /scraping-challenge

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
