from flask import Flask, jsonify, request
app = Flask(__name__)

id = 1
comidas = []

def create_comida(nome):
    global id
    comida = {
        'id': id, 
        'nome': nome
    }
    comidas.append(comida)
    id += 1
    return comida

def find_by_id(id):
    comida = [comida for comida in comidas if comida['id'] == id]
    if len(comida) == 0:
        return None
    return comida[0]

create_comida('Por Kilo')
create_comida('Escondidinho')

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/comidas')
def route_get_comidas():
    return response(comidas)

@app.route('/comidas/<int:id>')
def route_get_comida(id):
    comida = find_by_id(id)
    if comida is None:
        return 'Not Found', 404
    return response(comida)

def response(obj):
    resp = jsonify(obj)
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/comidas', methods=['POST'])
def route_create_comida():
    body = request.json
    comida = create_comida(body['nome'])
    return response(comida), 201

@app.route('/comidas/<int:id>', methods=['PUT'])
def route_update_comida(id):
    comida = find_by_id(id)
    if comida is None:
        return 'Not Found', 404
    body = request.json
    comida['nome'] = body['nome']
    return 'Alterado com sucesso'