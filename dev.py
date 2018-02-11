import requests
import datetime
import pytz
import constants as const
import json
import pprint


city = 'Los Angeles'
location = const.locations[city]
# seven_day_dt = [(datetime.datetime.now(tz=pytz.timezone(location.timezone)) - datetime.timedelta(days=days))
#                 for days in range(7)]
# seven_day_dt_isoformat = [dt.isoformat(timespec='seconds') for dt in seven_day_dt]
# location_dt = datetime.datetime.now(tz=pytz.timezone(location.timezone)) - datetime.timedelta(days=1)
# print(location_dt)
# location_dt_isoformat = location_dt.isoformat(timespec='seconds')
# print(location_dt_isoformat)
# print(seven_day_dt_isoformat)


# At this moment
# https://api.darksky.net/forecast/[key]/[latitude],[longitude]
# url = 'https://api.darksky.net/forecast/0050344aa077ab4bebd2bd0c63e18393/37.8267,-122.4233'


# Time machine request
seven_day_data = []
for days_back in range(3):

    # Day this week
    dt = datetime.datetime.now(tz=pytz.timezone(location.timezone)) - datetime.timedelta(days=days_back)
    dt_isoformat = dt.isoformat(timespec='seconds')

    # https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]
    url = f'https://api.darksky.net/forecast/0050344aa077ab4bebd2bd0c63e18393/' \
          f'{location.latitude},' \
          f'{location.longitude},' \
          f'{dt_isoformat}' \
          f'?exclude=currently,minutely,hourly,flags,offset'

    r = requests.get(url).text
    data = json.loads(r)['daily']['data'][0]

    # pp = pprint.PrettyPrinter()
    # pp.pprint(data)

    daily_data = {k: data[k] for k in ['summary', 'icon', 'temperatureHigh', 'temperatureLow', 'time']}
    seven_day_data.append(daily_data)

print(seven_day_data)

