from flask import Flask
from flask import request
import controllers as controllers
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def urlBase():
    return 'Servidor de profissionais da empresa'

@app.route('/profissionais', methods = ['GET'])
def listarProfissionais():
    return controllers.listarProfissionais()

@app.route('/profissionais', methods = ['POST'])
def criarProfissional():
   controllers.adicionarProfissional({'nome': 'Fernando', 'id': 3, 'data_contratacao': '13/02/2021', 'especialidade': 'Gestor de trafego pago'})
   controllers.adicionarProfissional({'nome': 'Lucas', 'id': 4, 'data_contratacao': '29/01/2015', 'especialidade': 'Analista de infraestrutura'})
   return "Profissionais adicionados com sucesso", 201

@app.route('/profissionais/<int:idProfissional>', methods = ['GET'])
def buscarProfissionalPorID(idProfissional):
    try:
        return controllers.profissionalID(idProfissional)
    except controllers.ProfissionalNaoEncontrado:
        return ({'erro': 'Profissional nao encontrado'}, 400)

# @app.route('/profissionais/<int:idProfissional>', methods = ['PUT'])
# def editarProfissionalPorID(idProfissional):
#     if not isinstance(idProfissional, int):
#         return "ID do profissional deve ser um número inteiro", 400
#     if not request.is_json:
#         return "Solicitação não contém dados JSON", 400
#     if 'nome' not in request.json.keys():
#         return "Nome não fornecido", 400

#     return "Profissional editado com sucesso", 200

app.run(host='0.0.0.0', port=5000, debug=True)