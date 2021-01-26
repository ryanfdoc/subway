
# Python Script to Print Next Trains Stopping at 96th Street

import os
import requests
import time

from underground import metadata, SubwayFeed

# Grab API Key from Env file
# API_KEY = os.getenv('MTA_API_KEY')

# Example of SubwayFeed command
# URL = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
# Route = '2'
# feed = SubwayFeed.get(URL)
# OR
# feed = SubwayFeed.get(ROUTE)

ROUTE1 = '1'
ROUTE2 = '2'
ROUTE3 = '3'

Feed1 = underground.SubwayFeed(ROUTE1,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')
Feed2 = underground.SubwayFeed(ROUTE2,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')
Feed3 = underground.SubwayFeed(ROUTE3,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')

Feed_ext1 = Feed1.extract_stop_dict()
Feed_ext2 = Feed2.extract_stop_dict()
Feed_ext3 = Feed3.extract_stop_dict()

# Hopefully this prints
