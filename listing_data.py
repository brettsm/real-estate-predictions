import requests
import pandas as pd
import json
from dotenv import load_dotenv
from dotenv import find_dotenv
import os

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')
print(api_key)
api_host = os.getenv('API_HOST')
print(api_host)
rent_url = os.getenv('URL_RENT')
print(rent_url)
listingQueryString = {"city":"New York City","state_code":"NY","offset":"0","limit":"50","sort":"relevance"}

headers1 = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": api_host
}

response = requests.get(rent_url, headers=headers1, params=listingQueryString)

print(type(response))

data = response.json()

print(list(data))

listings = data['properties']



df_listings = pd.DataFrame.from_dict(listings)

print(df_listings.head())

