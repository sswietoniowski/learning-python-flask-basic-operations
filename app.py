from flask import Flask
from flask import request
from flask import current_app

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    app_name = current_app.name
        
    return f"""
<h1>Hello World!</h1>
<p>Your browser is: {user_agent}.</p>
<p>Your app is: {app_name}.</p>
"""


@app.route('/user/<name>')
def user(name):    
    return f'<h1>Hello, {name}!</h1>'


if __name__ == '__main__':
    app.run()