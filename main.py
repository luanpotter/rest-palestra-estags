from flask import Flask, abort, jsonify
app = Flask(__name__)

todos = []

def get_next_id():
    ids = [todo['id'] for todo in todos]
    if len(ids) == 0:
        return 0
    return max(ids) + 1

def create_todo(text):
    return {
        'id': get_next_id(),
        'text': text,
    }

todos.append(create_todo('oi'))
todos.append(create_todo('dois'))

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to our TODO API!'

@app.route('/todos')
def list_todos():
    return jsonify(todos)

@app.route('/todos/<id>')
def get_todo(id):
    print(id)
    el = [todo for todo in todos if todo['id'] == int(id)]
    print(el)
    if len(el) == 0:
        abort(404)
    return jsonify(el[0])
