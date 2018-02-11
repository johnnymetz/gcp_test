from app import app
from flask import render_template, session, request, redirect, url_for, flash, Markup
# import pandas as pd
from helpers import *
import constants as const
import pytz


@app.route('/', methods=['GET', 'POST'])
def index():
    for k, default in [('my_locations', const.locations), ('city', 'Los Angeles')]:
        if k not in session:
            session[k] = default
    data = get_weather_data(
        app.config.get('API_KEY'),
        session['city'],
        session['my_locations'],
        app.config.get('NUMBER_OF_DAYS')
    )
    # data = []
    # for _ in range(4):
    #     day = {}
    #     for k in ['temperatureHigh', 'temperatureLow']:
    #         day[k] = 40
    #     day['summary'] = 'some summary'
    #     day['icon'] = 'partly-cloudy'
    #     from datetime import datetime
    #     day['dt'] = datetime.now()
    #     data.append(day)

    # df = pd.DataFrame(data)
    # df.to_pickle('data.pickle')

    # df = pd.read_pickle('data.pickle')
    # data = df.to_dict(orient='records')

    return render_template('index.html',
                           data=data,
                           cities=session['my_locations'].keys()
                           )


@app.route('/change_city', methods=['POST'])
def change_city():
    session['city'] = request.form['city']
    flash(Markup('City successfully updated to <b>{}</b>!'.format(session["city"])), category='success')
    return redirect(url_for('index'))


@app.route('/add_city', methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        location = dict(
            latitude=float(request.form['latitude']),
            longitude=float(request.form['longitude']),
            tz=request.form['tz']
        )
        city_name = request.form['city']
        session['my_locations'][city_name] = location
        flash(Markup('City <b>{}</b> successfully added!'.format(city_name)), category='success')
    return render_template('add_city.html', common_timezones=pytz.common_timezones)


# @app.route('/clear')
# def clear():
#     session.clear()
#     flash('Session cleared', category='success')
#     return redirect(url_for('index'))
