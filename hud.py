from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Hogan"

@app.route('/test')
def test(name="no one"):
    name = request.args.get('name', name)
    return 'Hello from {}!'.format(name)

@app.route('/test/<int:num1>/<int:num2>')
def name_test(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)

app.run(debug=True, port=8000, host='0.0.0.0')

