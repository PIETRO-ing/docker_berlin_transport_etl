# docker_berlin_transport_etl
real time delay departures from U Bahn Alexanderplatz.

The workflow using Docker Compose:

-Scraping the Berlin Transportaion API (https://v5.vbb.transport.rest/getting-started.html) and retrieving all the real time departures from U Bahn Alexanderplatz;

-Storing the information to MongoDB database;

-Building an ETL job that extract data from MongoDB, store in Postgres database, using quiery to extract all the delay departures taking place at U Bahn Alexanderplatz and send to SlackBot app to see the information that is constantly updated

