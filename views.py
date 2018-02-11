from app import app
from flask import render_template, session, request, redirect, url_for, flash, Markup
# import pandas as pd
from helpers import *
import constants as const
import pytz


@app.route('/', methods=['GET', 'POST'])
def index():
    for k, default in [('all_cities', const.locations), ('city', 'Los Angeles')]:
        if k not in session:
            session[k] = default
    data = get_weather_data(session['city'])
    # df = pd.DataFrame(data)
    # df.to_pickle('data.pickle')

    # # DEV
    # df = pd.read_pickle('data.pickle')
    # data = df.to_dict(orient='records')

    return render_template('index.html',
                           data=data,
                           cities=session['all_cities'].keys()
                           )


@app.route('/change_city', methods=['POST'])
def change_city():
    session['city'] = request.form['city']
    flash(Markup('City successfully updated to <b>{}</b>!'.format(session["city"])), category='success')
    return redirect(url_for('index'))


@app.route('/add_city', methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        location = const.Location(
            latitude=int(request.form['latitude']),
            longitude=int(request.form['longitude']),
            timezone=request.form['timezone']
        )
        session['all_cities'][request.form['city']] = location
    return render_template('add_city.html', common_timezones=pytz.common_timezones)


@app.route('/clear')
def clear():
    session.cler()
    flash('Session cleared', category='success')
    return redirect(url_for('index'))
