from flask import Flask
from flask import Response
from flask import request
import json

app = Flask(__name__)

class Blab:
    def __init__(self, id, postTime, author, message):
        self.id = id
        self.postTime = postTime
        self.author = author
        self.message = message

    def toDict(self):
        return {
            "id": self.id,
            "postTime": self.postTime,
            "author": self.author,
            "message": self.message
        }

Blabs = [Blab(1, 0, {"email": "johndoe@yahoo.com", "name": "John Doe"}, "Hello World")]

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


@app.route('/blabs', methods=['GET', 'POST'])
def blabs():
    if request.method == 'GET':
        result = []
        for blab in Blabs:
            result.append(blab.toDict())
        return Response(json.dumps(result), mimetype='application/json')
    elif request.method == 'POST':
        print(request.json)
        author = request.json['author']
        message = request.json['message']
        blab = Blab(len(Blabs) + 1, len(Blabs), author, message)
        Blabs.append(blab)
        return Response(json.dumps(blab.toDict()), mimetype='application/json')


@app.route('/blabs/<id>', methods=['DELETE'])
def delete_blab(id):
    if request.method == 'DELETE':
        index = find_blab_by_id(id)
        if index != -1:
            result = Blab(Blabs[index].id, Blabs[index].postTime, Blabs[index].author, Blabs[index].message).toDict()
            del Blabs[index]
            return Response(json.dumps(result), mimetype='application/json')


def find_blab_by_id(id):
    for i in range(len(Blabs)):
        if Blabs[i].id == id:
            return i
    return -1



if __name__ == '__main__':
    app.run(debug=True)