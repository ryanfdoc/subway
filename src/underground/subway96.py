# Python Script to Print Next Trains Stopping at 96th Street

import os
import requests
import time
import underground

from underground import metadata, SubwayFeed

# Grab API Key from Env file
# API_KEY = os.getenv('MTA_API_KEY')

# Example of SubwayFeed command
# URL = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
# Route = '2'
# feed = SubwayFeed.get(URL)
# OR
# feed = SubwayFeed.get(ROUTE)

ROUTE = '1'
feed = SubwayFeed.get(ROUTE,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')

print "Really Hope this Works. WAR EAGLE"
pprint.pprint(feed.extract_stop_dict())

# Hopefully this prints
