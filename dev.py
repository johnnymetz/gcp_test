import requests
import urllib2
import datetime
import pytz
import constants as const
import json
import pprint


city = 'Los Angeles'
location = const.locations[city]

dt = datetime.datetime.now(tz=pytz.timezone(location['tz'])) - datetime.timedelta(days=1)
# dt_isoformat = dt.isoformat(timespec='seconds')  # py3 only
dt_isoformat = dt.replace(microsecond=0).isoformat()  # py2 + py3 compatible


# At this moment
# https://api.darksky.net/forecast/[key]/[latitude],[longitude]
# url = 'https://api.darksky.net/forecast/0050344aa077ab4bebd2bd0c63e18393/37.8267,-122.4233'


# https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]
url = 'https://api.darksky.net/forecast/{}/{},{},{}' \
      '?exclude=currently,minutely,hourly,flags,offset'.format(
    '0050344aa077ab4bebd2bd0c63e18393',
    location['latitude'],
    location['longitude'],
    dt_isoformat
)
r = requests.get(url).text
response = urllib2.urlopen(url)
data = json.loads(response.read())['daily']['data'][0]
print(data)
print(type(data))
# data2 = json.loads(response)['daily']['data'][0]
# print(data2)
#
data2 = json.loads(r)['daily']['data'][0]
print(data2)
print(data == data2)