import json
from flask import Flask, Response, request
app = Flask(__name__)

id = 1
items = []

def create_item(nome):
    global id
    item = {
        'id': id,
        'nome': nome,
    }
    items.append(item)
    id += 1
    return item

def response(obj):
    r = Response(json.dumps(obj))
    r.headers['Content-Type'] = 'application/json'
    return r

def get_by_id(id):
    for item in items:
        if item['id'] == id:
            return item

create_item('item 1')
create_item('item 2')

@app.route('/')
def route_hello():
    return 'Hello World!'

@app.route('/items')
def route_items():
    return response(items)

@app.route('/items', methods=['POST'])
def route_create_item():
    body = request.json
    item = create_item(body['nome'])
    return response(item), 201

@app.route('/items/<int:id>')
def route_items_by_id(id):
    item = get_by_id(id)
    if item is None:
        return "Not Found", 404
    return response(item)

@app.route('/items/<int:id>', methods=['PUT'])
def route_update_item(id):
    item = get_by_id(id)
    if item is None:
        return "Not Found", 404
    body = request.json    
    item['nome'] = body['nome']
    return "OK", 202

@app.route('/items/<int:id>', methods=['DELETE'])
def route_delete_item(id):
    item = get_by_id(id)
    if item is None:
        return "Not Found", 404
    body = request.json
    items.remove(item)
    return "OK"

    
# [item for item in items if item['id'] != id]

# for index in range(len(items)):
#   item = items[index]
#   if item['id'] == id
#       items.pop(index)
#       break

# for item in items:
#   if item['id'] == id:
#       items.remove(item)
#       break

# for index, item in enumerate(items):
#    if item['id'] == id:
#         items.pop(index)
#         break