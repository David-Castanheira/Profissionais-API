from flask import Flask
from flask import request
import controllers.ProfissionaisController as ProfissionaisController

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def urlBase():
    return 'Servidor de profissionais da empresa'

# Rota GET - Retorna a lista de profissionais cadastrados
@app.route('/profissionais', methods = ['GET'])
def listarProfissionais():
    return ProfissionaisController.listarProfissionais()

# Rota POST - Retorna a lista de profissionais que foram adicionados 
@app.route('/profissionais', methods = ['POST'])
def criarProfissional():
   ProfissionaisController.adicionarProfissional({'nome': 'Fernando', 'id': 3, 'data_contratacao': '13/02/2021', 'especialidade': 'Gestor de trafego pago'})
   ProfissionaisController.adicionarProfissional({'nome': 'Lucas', 'id': 4, 'data_contratacao': '29/01/2015', 'especialidade': 'Analista de infraestrutura'})
   return "Profissionais adicionados com sucesso", 201

# Rota GET - Faz uma busca de profissionais pelo ID
@app.route('/profissionais/<int:idProfissional>', methods = ['GET'])
def buscarProfissionalPorID(idProfissional):
    try:
        return ProfissionaisController.profissionalID(idProfissional)
    except ProfissionaisController.ProfissionalNaoEncontrado:
        return ({'erro': 'Profissional nao encontrado'}, 400)

# Tentativa 1 da rota PUT
# @app.route('/profissionais/<int:idProfissional>', methods = ['PUT'])
# def editarProfissionalPorID(idProfissional):
#     if not isinstance(idProfissional, int):
#         return "ID do profissional deve ser um número inteiro", 400
#     if not request.is_json:
#         return "Solicitação não contém dados JSON", 400
#     if 'nome' not in request.json.keys():
#         return "Nome não fornecido", 400

#     return "Profissional editado com sucesso", 200

# Tentativa 2 da rota PUT
# @app.route('/profissionais/<int:idProfissional>', methods = ['PUT'])
# def editarProfissionalPorID(idProfissional):
#     detalhes_profissional = request.get_json()
#     nova_especialidade = detalhes_profissional.put('nova_especialidade')
#     controllers.editarProfissional(idProfissional, nova_especialidade)

#     if controllers.dados['profissionais'] != nova_especialidade:
#        return "Profissionais alterados com sucesso", 201
#     else:
#        return ({'erro': 'Profissional nao encontrado'}, 400)

# Tentativa 3 da rota PUT
# @app.route('/profissionais/<int:idProfissional>', methods = ['PUT'])
# def editarProfissionalPorID(idProfissional):
#     if 'especialidade' not in request.json.keys():
#         return ({'erro': 'Profissional sem especialidade definida'}, 400)
#     nova_especialidade = request.json['especialidade']
#     try:
#         controllers.editarProfissional(idProfissional, nova_especialidade)
#         return controllers.profissionalID(idProfissional)
#     except controllers.ProfissionalNaoEncontrado:
#         return ({'erro': 'Profissional nao encontrado'}, 400)

# Tentativa 4 da rota PUT - Bad Request (Corrigir o erro)
@app.route('/profissionais/<int:idProfissional>', methods = ['PUT'])
def editarProfissionalPorID(idProfissional):
   data = request.get_json(force=True)
   if 'especialidade' not in data.keys():
       return ({'erro': 'Profissional sem especialidade definida'}, 400)
   nova_especialidade = data['especialidade']
   try:
       ProfissionaisController.editarProfissional(idProfissional, nova_especialidade)
       return ProfissionaisController.profissionalID(idProfissional)
   except ProfissionaisController.ProfissionalNaoEncontrado:
       return ({'erro': 'Profissional nao encontrado'}, 400)

# Rota Delete - Retorna uma lista com os profissionais removidos 
@app.route('/profissionais/<int:idProfissional>', methods = ['DELETE'])
def apagarProfissionalPorID(idProfissional):
    try:
        ProfissionaisController.apagarProfissional(idProfissional)
        return "Profissionais removidos com sucesso", 201
    except ProfissionaisController.ProfissionalNaoEncontrado:
        return ({'erro': 'Profissional nao encontrado'}, 400)

app.run(host='0.0.0.0', port=5000, debug=True)