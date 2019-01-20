
rom flask import Flask, abort, jsonify, request
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

@app.route('/todos/<int:id>', methods=['GET'])
def route_get_todo(id):
    el = [todo for todo in todos if todo['id'] == id]
    if len(el) == 0:
        abort(404)
    return jsonify(el[0])

@app.route('/todos', methods=['POST'])
def route_create_todo():
    body = request.json
    return jsonify(create_todo(body['text']))

@app.route('/todos/<int:id>', methods=['DELETE'])
def route_delete_todo(id):
    global todos
    el = [todo for todo in todos if todo['id'] == id]
    if len(el) == 0:
        abort(404)
    todos = [todo for todo in todos if todo['id'] != id]
    return jsonify(el[0])

@app.route('/todos/<int:id>', methods=['PUT'])
def route_update_todo(id):
    el = [todo for todo in todos if todo['id'] == id]
    if len(el) == 0:
        abort(404)
    todo = el[0]
    body = request.json
    todo['text'] = body['text']
    return jsonify(todo)

@app.route('/todos/<int:id>', methods=['POST'])
def route_create_todo_with_id(id):
    el = [todo for todo in todos if todo['id'] == id]
    if len(el) != 0:
        abort(422, 'Id you are trying to create already exists')
    body = request.json
    todo = {
        'id': id,
        'text': body['text']
    }
    todos.append(todo)
    return jsonify(todo)
