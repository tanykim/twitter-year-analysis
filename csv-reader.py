import csv
from datetime import datetime
import json
import pytz

DEFAULT_TIMEZONE = pytz.timezone('America/Los_Angeles')
YEAR = 2013

data_of_year = []

def addDate(date):
    data_of_year.insert(0, dict(date=date, value=1))

def getTweetInfo(d):
    date = d.strftime('%-m/%-d/%-Y')
    if len(data_of_year) == 0:
        addDate(date)
    else:
        print (data_of_year[0]['date'], date)
        if data_of_year[0]['date'] == date:
            data_of_year[0]['value'] += 1
        else:
            addDate(date)

with open('tweets.csv', newline='') as csvfile:
    sheet = csv.DictReader(csvfile)
    for row in sheet:
        utc_date = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S %z')
        date = utc_date.astimezone(DEFAULT_TIMEZONE)
        year = int(date.year)
        if year == YEAR:
            getTweetInfo(date)
        elif year < YEAR:
            break


fd = open('data-' + str(YEAR) + '.json', 'w', encoding='utf8')
json_data = json.dumps(data_of_year, separators=(',',':'), indent=2, ensure_ascii=False)
fd.write(json_data)
fd.close()
