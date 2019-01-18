from flask import Flask, abort, jsonify, request
app = Flask(__name__)

todos = []

def get_next_id():
    ids = [todo['id'] for todo in todos]
    if len(ids) == 0:
        return 0
    return max(ids) + 1

def create_todo(text):
    todo = {
        'id': get_next_id(),
        'text': text,
    }
    todos.append(todo)
    return todo

create_todo('oi')
create_todo('dois')

@app.route('/', methods=['GET'])
def route_hello_world():
    return 'Hello, World! Welcome to our TODO API!'

@app.route('/todos', methods=['GET'])
def route_list_todos():
    return jsonify(todos)

@app.route('/todos/<id>', methods=['GET'])
def route_get_todo(id):
    el = [todo for todo in todos if todo['id'] == int(id)]
    if len(el) == 0:
        abort(404)
    return jsonify(el[0])

@app.route('/todos', methods=['POST'])
def route_create_todo():
    body = request.json
    return jsonify(create_todo(body['text']))
