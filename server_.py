from flask import Flask, jsonify
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)

def my_task():
    result = sum(range(1, 1000000))
    return result



@app.route('/run-task')
def run_task():
    return jsonify({'status': 'ok','result': my_task()})



@app.route('/sum')
def sum_ab():
    a=5
    b=3
    return str(a+b)



@app.route('/')
def home():
    return 'Сервер работает'




if __name__ == '__main__':
    app.run(port=5000)