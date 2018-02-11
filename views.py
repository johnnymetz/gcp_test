from app import app
from flask import render_template, session, request, redirect, url_for, flash, Markup
import pandas as pd
from helpers import *
import constants as const


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'city' not in session:
        session['city'] = 'Los Angeles'
    # data = get_weather_data(session['city'])
    # df = pd.DataFrame(data)
    # df.to_pickle('data.pickle')

    # DEV
    df = pd.read_pickle('data.pickle')
    data = df.to_dict(orient='records')

    return render_template('index.html',
                           data=data,
                           cities=const.locations.keys()
                           )


@app.route('/change_city', methods=['POST'])
def change_city():
    session['city'] = request.form['city']
    flash(Markup(f'City successfully updated to <b>{session["city"]}</b>!'), category='success')
    return redirect(url_for('index'))


@app.route('/clear')
def clear():
    session.cler()
    flash('Session cleared', category='success')
    return redirect(url_for('index'))
