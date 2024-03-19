#!/usr/bin/python3
'''A simple Flask web application.
'''


from flask import Flask, render_template






app = Flask(__name__)
''' Flask  instance.'''
app.url_map.strict_slashes = False


@app.route('/')



def index():
    ''' home.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb page.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''python page.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''  page.'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''number template page.'''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
