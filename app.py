from asyncio import tasks
from flask import Flask, jsonify, request 
from models.missao import Missao

# Cria uma nova instância da classe Flask, atribuindo-a à variável app
# o __name__ tem valor __main__
app = Flask(__name__) 

missoes = [] #lista vazia que armazenará as missões criadas
controle_de_missao_pelo_id = 1 #Uma variável global que controla o ID da próxima missão a ser criada, iniciando em 1.
@app.route('/missoes', methods=['POST'])
def create_mission():
    global controle_de_missao_pelo_id
    data = request.get_json() #recupera os dados JSON enviados no corpo da requisição POST.
    nova_missao = Missao(id=controle_de_missao_pelo_id, nome_da_missao=data.get('nome_da_missao'), data_de_lancamento=data.get('data_de_lancamento'), destino=data.get('destino'), tripulacao=data.get('tripulacao'), duracao=data.get('duracao'), status_da_missao=data.get('status_da_missao'), carga_util=data.get('carga_util'))
    controle_de_missao_pelo_id += 1
    missoes.append(nova_missao)
    print(missoes)
    return jsonify({"message": "Nova missão criada com sucesso."})

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=2961) 