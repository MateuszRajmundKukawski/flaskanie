__author__ = 'mati'
from flask import Flask, g
import os
import sqlite3
from datetime import datetime
from flask import flash, redirect, url_for, request, render_template
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = 'bardzosekretnawartosc',
    DATABASE = os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME = 'Moje zadania'
))


def connect_db():
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
    error = None

    if request.method == 'POST':
        if len(request.form['zadanie']) > 0:
            zadanie = request.form['zadanie']
            zrobione = '0'
            data_pub = datetime.now()
            db = get_db()
            db.execute('insert into zadania (zadanie, zrobione, data_pub) values (?, ?, ?);',
                       [zadanie, zrobione, data_pub])
            db.commit()
            flash('Dodano nowe zadanie.')
            return redirect(url_for('index'))

        error = u'Nie mozesz dodac pustego zadania!'
    db = get_db()
    kursor = db.execute('select * from zadania order by data_pub desc;')
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania, error=error)


@app.route('/zrobione', methods=['POST'])
def zrobione():
    """Zmiana statusu zadania na wykonane."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('update zadania set zrobione=1 where id=?', [zadanie_id, ])
    db.commit()
    return redirect(url_for('index'))


@app.route('/usun2', methods=['POST'])
def usun():
    """Zmiana statusu zadania na wykonane."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('delete from zadania where id=?', [zadanie_id, ])
    db.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
