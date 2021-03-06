import requests
import time
import logging
import pymongo



# Create a connection to the MongoDB database server
client = pymongo.MongoClient(host='mongodb')


# Create/use a database
db = client.departures

# Define the collection
collection = db.departures_table




# get the id of U_Alexanderplatz for the query:
response_id = requests.get('https://v5.vbb.transport.rest/locations?query=alexanderplatz&results=1')
response_id.json()[0]['id']

while True: #our own little data streamer / server!
    response_departures=requests.get('https://v5.vbb.transport.rest/stops/900100003/departures?duration=1&when=now')
    dep_json = response_departures.json()
    count = 0
    while count < len(response_departures.json()):
        departures_from = response_departures.json()[count]['stop']['name']
        direction = response_departures.json()[count]['direction']
        delay = response_departures.json()[count]['delay']
        time_schedule = response_departures.json()[count]['when'] 
        departures_realtime= {'departures_from': departures_from, 'direction': direction, 'delay':delay,'time_schedule':time_schedule}
        #logging.critical(f"dep. from: {dep_from}\ndirection: {direction}\ndelay: {delay}\nwhen: {when}\n\n\n")
        collection.insert(departures_realtime)
        logging.critical(departures_realtime)
        count+=1
    time.sleep(10)













