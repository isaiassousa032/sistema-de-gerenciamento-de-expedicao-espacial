from flask import Flask, jsonify, request 
from models.missao import Missao

# Cria uma nova instância da classe Flask, atribuindo-a à variável app
# o __name__ tem valor __main__
app = Flask(__name__) 

missoes = [] #lista vazia que armazenará as missões criadas
controle_de_missao_pelo_id = 1 #Uma variável global que controla o ID da próxima missão a ser criada, iniciando em 1.
@app.route('/missoes', methods=['POST'])
def cria_missao():
    global controle_de_missao_pelo_id
    data = request.get_json() #recupera os dados JSON enviados no corpo da requisição POST.
    nova_missao = Missao(id=controle_de_missao_pelo_id, nome_missao=data.get('nome_missao'), data_lancamento=data.get('data_lancamento'), destino=data.get('destino'), estado_missao=data.get('estado_missao'), tripulacao=data.get('tripulacao'), carga_util=data.get('carga_util'), duracao_missao=data.get('duracao_missao'), custo_missao=data.get('custo_missao'), status_missao=data.get('status_missao'), )
    controle_de_missao_pelo_id += 1
    missoes.append(nova_missao)
    print(missoes)
    return jsonify({"message": "Nova missão criada com sucesso."})

@app.route('/missoes', methods=['GET'])
def recupera_missoes():
    # Ordena as missões por data de lançamento em ordem decrescente
    missoes_ordenadas = sorted(missoes, key=lambda m: m.data_lancamento, reverse=True)

    lista_missoes = [missao.para_dicionario() for missao in missoes_ordenadas] #itera cada missao utilizando a classe missao.para_dicionario que retorna em formato json
    output = {
                "missoes": lista_missoes,
                "total_missoes": len(lista_missoes)
            }
    return jsonify(output)

@app.route('/missoes/<int:id>', methods=['GET'])
def recupera_missao_por_id(id):
    for m in missoes:
        if m.id == id:
            return jsonify(m.para_dicionario())
    return jsonify({"message": "Missão não encontrada"}), 404

@app.route('/missoes/<int:id>', methods=['PUT'])
def atualiza_missao(id):
    missao = None #é adicionado porque pode ou não, ter uma tarefa e se nao tiver retorna None
    for m in missoes:
        if m.id == id:
            missao = m
            break
    
    if missao == None:
        return jsonify({"message": "Missão não encontrada"}), 404 #404 é uma mensagem do servidor, avisando que o recurso/página não foi encontrado.
    
    data = request.get_json()
    missao.nome_missao = data['nome_missao']
    missao.data_lancamento = data['data_lancamento']
    missao.destino = data['destino']
    missao.estado_missao = data['estado_missao']
    missao.tripulacao = data['tripulacao']
    missao.carga_util = data['carga_util']
    missao.duracao_missao = data['duracao_missao']
    missao.custo_missao = data['custo_missao']
    missao.status_missao = data['status_missao']
    
    
    return jsonify({"message":"Missão atualizada com sucesso."}), 200
           
@app.route('/missoes/<int:id>', methods=['DELETE'])
def deleta_missao(id):
    missao = None
    for m in missoes:
        if m.id == id:
            missao = m
            break #é usado para não precisar percorrer todo o array mesmo tendo achado o elemento procurado, assim economizando processamento

    if not missao:
        return jsonify({"message": "Missão não encontrada"}), 404
    
    missoes.remove(missao)
    return jsonify({"message": "Missão deletada com sucesso"}), 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=2961) 