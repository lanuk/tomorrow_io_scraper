FROM python:3.10

WORKDIR /scraper

RUN apt-get update && apt-get install cron -y 

COPY . .

RUN crontab ./crontab
RUN pip install -r requirements.txt

CMD ["python", "scraper.py"]