import urllib2
import datetime
import pytz
import json


def get_weather_data(api_key, city, my_locations, number_of_days):
    """
    Get weather data from the last several days, including today.

    :return: list of dictionaries containing data for last several days
    """
    # Get Location data
    location = my_locations[city]

    # Time machine request
    multiple_day_data = []
    for days_back in range(number_of_days):
        # Day this week
        dt = datetime.datetime.now(tz=pytz.timezone(location['tz'])) - datetime.timedelta(days=days_back)
        # dt_isoformat = dt.isoformat(timespec='seconds')  # py3 only
        dt_isoformat = dt.replace(microsecond=0).isoformat()  # py2 + py3 compatible

        # https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]
        url = 'https://api.darksky.net/forecast/{}/{},{},{}' \
              '?exclude=currently,minutely,hourly,flags,offset'.format(
            api_key,
            location['latitude'],
            location['longitude'],
            dt_isoformat
        )

        # Grab data from weather api
        response = urllib2.urlopen(url).read()
        data = json.loads(response)['daily']['data'][0]

        # Grab data points we want to display to user
        daily_data = {k: data[k] for k in ['summary', 'icon', 'temperatureHigh', 'temperatureLow', 'time']}
        daily_data['dt'] = dt
        multiple_day_data.append(daily_data)
    return multiple_day_data
