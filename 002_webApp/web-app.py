# Firstly Should install Flask (http://flask.pocoo.org)
# pip install Flask
from flask import Flask, request, render_template
# Create WebApplication Object:
app = Flask(__name__)


@app.route('/')
def this_is_default_func_with_useless_name_that_called_by_route_open():
    return "<a href='/hello/'>Welcome! Start here:</a>"


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    """
    Multi-Lines comments are created by Triple quotes marks!
    That is recommended for Code Description Documentation.
    """
    if request.method == 'POST':
        name = request.form['name']  # Get name-Variable from Request
    else:
        name = None
    return render_template('hello_form.html', name=name)


@app.route('/<name>')
def hello_buddy(name):
    """
    ALL OTHERS Routes are Read as NAME-Variable!
    """
    return 'Hello, ' + name + '!'


# APPLICATION START : If This File Is Main!
if __name__ == '__main__':  # Deafult Address - http://localhost:5000/
    app.run()
