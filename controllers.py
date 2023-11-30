dados = {'profissionais': [
        {'nome': 'Diego', 'id': 1, 'data_contratacao': '12/10/2001', 'especialidade': 'Desenvolvedor de Sistemas'},
        {'nome': 'Maria', 'id': 2, 'data_contratacao': '23/04/2010', 'especialidade': 'Social Media'}
        ]}

class ProfissionalNaoEncontrado(Exception):
    pass

def profissionalID(id_profissional):
    lista_profissionais = dados['profissionais']
    for dic in lista_profissionais:
        if dic['id'] == id_profissional:
            return dic
    raise ProfissionalNaoEncontrado

def profissionalExiste(id_profissional):
    try:
        profissionalID(id_profissional)
        return True
    except ProfissionalNaoEncontrado:
        return False
    
def adicionarProfissional(dic):
    dados['profissionais'].append(dic)

def listarProfissionais():
    return dados['profissionais']

def resetar():
    dados['profissionais'] = []

def apagarProfissional(id_profissional):
    dic_profissionais = profissionalID(id_profissional)
    dados['profissionais'].remove(dic_profissionais)

def editarProfissional(id_profissional, nova_especialidade):
    dic_profissionais = profissionalID(id_profissional)
    dic_profissionais['especialidade'] = nova_especialidade