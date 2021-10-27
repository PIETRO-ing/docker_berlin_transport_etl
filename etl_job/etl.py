import time
import pymongo
import logging


logging.critical("Hello World")

while True:

    time.sleep(10)  # seconds

    # Establish a connection to the MongoDB server
    client = pymongo.MongoClient("mongodb")

    # Select the database you want to use withing the MongoDB server
    db = client.departures

    # Select the collection of documents you want to use withing the MongoDB database
    collection = db.departures_table


    # connect to postgres
    from sqlalchemy import create_engine



    pg = create_engine('postgres://postgres:postgres@postgresdb:5432/departuresPG', echo=True)
    pg.execute('''
        CREATE TABLE IF NOT EXISTS departures_table (
        departures_from varchar(70),
        direction varchar(70),
        delay NUMERIC,
        time_schedule timestamptz

    );
    ''')

    # print all entries
    entries = collection.find()
    for e in entries:
    
        departures_from = e['departures_from']
        direction = e['direction']
        delay = e['delay']
        time_schedule = e['time_schedule']
    
        query = "INSERT INTO departures_table VALUES (%s, %s, %s, %s);"
        pg.execute(query, (departures_from, direction, delay, time_schedule))
    
        logging.critical(e)
    time.sleep(10)

    
