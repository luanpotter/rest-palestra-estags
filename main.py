from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to our TODO API!'

@app.route('/todos/<id>')
def get_todo(id):
    print(id)
    return 'id: %s' % id
