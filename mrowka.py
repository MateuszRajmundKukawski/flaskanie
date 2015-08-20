#-*- coding: utf-8 -*-
__author__ = 'mati'

from flask import Flask, render_template





app = Flask(__name__)


# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))


# lista pytań
PYTANIA = [
    {
        'pytanie': u'Stolica Hiszpani, to:',# pytanie
        'odpowiedzi': [u'Madryt', u'Warszawa', u'Barcelona'], # możliwe odpowiedzi
        'odpok': u'Madryt', # poprawna odpowiedź
    },
    {
        'pytanie': u'Objętość sześcianu o boku 6 cm, wynosi:',
        'odpowiedzi': [u'36', u'216', u'18'],
        'odpok': u'216',
    },
    {
        'pytanie': u'Symbol pierwiastka Helu, to:',
        'odpowiedzi': [u'Fe', u'H', u'He'],
        'odpok': u'He',
    }
]

from flask import request, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp_u in odpowiedzi.items():
            if odp_u == PYTANIA[int(pnr)]['odpok']:
                punkty += 1

        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(punkty), u'Wiewiorki sa smieszne')
        return redirect(url_for('home'))

    #return 'Cześć, tu Python!'
    return render_template('index.html', pytania=PYTANIA)


@app.route('/home')
def home():
    return render_template('home.html')








if __name__ == '__main__':
    app.run(debug=True)