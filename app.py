from flask import Flask
from flask import request
from flask import current_app
from flask import make_response
from flask import redirect
from flask import url_for
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    app_name = current_app.name
    response_content = f"""
<h1>Hello World!</h1>
<p>Your browser is: {user_agent}.</p>
<p>Your app is: {app_name}.</p>
<p>This document carries a cookie!</p>
"""        
    response = make_response(response_content)
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):    
    if  name != "jdoe":
        abort(404)
    return f'<h1>Hello, {name}!</h1>'


@app.route('/bad')
def bad():
    return '<h1>Bad Request!</h1>', 400


@app.route('/redirect')
def redirect_to():
    return redirect('/')


if __name__ == '__main__':
    app.run()