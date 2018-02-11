import requests
import datetime
import pytz
import constants as const
import json


def get_weather_data(city):
    """
    Get weather data from the last several days, including today.

    :return: list of dictionaries containing data for last several days
    """
    # Get Location data
    location = const.locations[city]

    # Time machine request
    multiple_day_data = []
    for days_back in range(7):
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
        daily_data['dt'] = dt
        multiple_day_data.append(daily_data)
    return multiple_day_data
