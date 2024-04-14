#!/bin/sh

CRON_FILE=/scraper/scraper_cron

crontab $CRON_FILE

crond -f -d 5
crontab -l