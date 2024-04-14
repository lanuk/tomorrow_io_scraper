FROM python:3.10-alpine

WORKDIR /scraper

RUN apk add build-base

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /scraper/scraper_cron.sh
CMD ["/scraper/scraper_cron.sh"]