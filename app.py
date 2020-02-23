from flask import Flask
from flask import Response
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'


@app.route('/greetings')
def greetings():
    greetings_arr = [
        {'index': 0, 'greeting': 'Hello'},
        {'index': 1, 'greeting': "What's up?"},
        {'index': 2, 'greeting': 'Hey man'},
        {'index': 3, 'greeting': "What's crackin?"},
    ]
    return Response(json.dumps(greetings_arr), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)