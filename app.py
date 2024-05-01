from asyncio import tasks
from flask import Flask, jsonify, request 
from models.missao import Missao

# Cria uma nova instância da classe Flask, atribuindo-a à variável app
# o __name__ tem valor __main__
app = Flask(__name__) 

missions = [] #lista vazia que armazenará as missões criadas
mission_id_control = 1 #Uma variável global que controla o ID da próxima missão a ser criada, iniciando em 1.
@app.route('/missions', methods=['POST'])
def create_mission():
    global mission_id_control
    data = request.get_json() #recupera os dados JSON enviados no corpo da requisição POST.
    new_mission = Missao(id=mission_id_control, nome_da_missao=data.get('nome_da_missao'), data_de_lancamento=data.get('data_de_lancamento'), destino=data.get('destino'), estado=data.get('estado'), tripulacao=data.get('tripulacao'), duracao=data.get('duracao'), status=data.get('status'), carga_util=data.get('carga_util'))
    mission_id_control += 1
    missions.append(new_mission)
    print(missions)
    return jsonify({"message": "Nova missão criada com sucesso."})
if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=2961) 