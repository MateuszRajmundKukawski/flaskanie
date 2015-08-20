__author__ = 'mati'

from flask import Flask, render_template, g, redirect, url_for, request
import os
import sqlite3


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = 'bardzosekretnawartosc',
    DATABASE = os.path.join(app.root_path, 'db.sqlite2'),
    SITE_NAME = 'Moje zadania'
))

def connect_db():
    #rv = sqlite3.connect(app.config['DATBASE'])
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db

@app.teardown_request
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/', methods=['GET', 'POST'])
def index():

    startloop = 0
    endloop = 4
    tooo = 1
    if request.method == 'POST':

        return redirect(url_for('index2'))
    #return 'KORN'
    elif request.method == 'GET':
        db = get_db()
        kurosr = db.execute('select * from zadania order by id;')


        zadania = kurosr.fetchall()

        return render_template('nowyMyk.html', zadania = zadania, startloop=startloop, endloop=endloop,tooo=tooo)

@app.route('/k', methods=['GET', 'POST'])
def index2():

    startloop = 4
    endloop = 8
    #tooo = 'kot'
    if request.method == 'POST':

        return redirect(url_for('index'))
    #return 'KORN'
    elif request.method == 'GET':
        db = get_db()
        kurosr = db.execute('select * from zadania order by id;')


        zadania = kurosr.fetchall()

        return render_template('nowyMyk.html', zadania = zadania, startloop=startloop, endloop=endloop)

if __name__ == '__main__':
    app.run(debug=True)
