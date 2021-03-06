import time
import requests
import logging
import pymongo
import slack
import pandas as pd
from sqlalchemy import create_engine
from pandas.io.json import json_normalize

webhook_url = "https://hooks.slack.com/services/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"

#joke = pyjokes.get_joke()

#create connection with postgres

#pg = create_engine('postgres://postgres:postgres@postgresDB:5432/departuresPG', echo=True)
#logging.critical("heyheyhey")
#delay_dep = pg.execute("SELECT distinct * FROM departures_table WHERE delay!=0 ORDER BY time_schedule ASC;")
#logging.critical(str(delay_dep))
#output=(f'Delay departures from {delay_dep}')
#data = {'delay': output}
#requests.post(url=webhook_url, json = data)


time.sleep(5)
pg = create_engine('postgres://postgres:postgres@postgresdb:5432/departuresPG', echo=False)
# query to select the departures on delay at U Alexanderplatz
query = 'SELECT DISTINCT * FROM departures_table WHERE delay!=0 ORDER BY time_schedule ASC;'
time.sleep(20)

while True:
    dep = pd.read_sql_query(query, con=pg)
    #logging.critical(dep)
    data1 = str(dep)
    #data = dep.to_json()
    #logging.critical(data)
    data = {'text': data1}
    requests.post(url=webhook_url, json=data)
    logging.critical(data)
    time.sleep(80)
