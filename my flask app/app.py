from flask import Flask, render_template, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/hey')
def hey_everybody():
    return redirect(url_for('hello'))

#custumized route based on user information - hold on variables
@app.route('/user/<username>')
def user(username):
    return 'Welcome user: %s' %escape(username)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#Handling errors / Redirecting it to a customized error page
@app.errorhandler(404)
def error(error):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)