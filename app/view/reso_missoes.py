from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missoes import Missoes

#para criar
argumentos_criacao = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos_criacao.add_argument('id', type=int)
argumentos_criacao.add_argument('nome_missao', type=str)
argumentos_criacao.add_argument('data_lancamento', type=str)
argumentos_criacao.add_argument('destino', type=str)
argumentos_criacao.add_argument('estado_missao', type=str)
argumentos_criacao.add_argument('tripulacao', type=str)
argumentos_criacao.add_argument('carga_util', type=str)
argumentos_criacao.add_argument('duracao_missao', type=str)
argumentos_criacao.add_argument('custo_missao', type=str)
argumentos_criacao.add_argument('status_missao', type=str)

#para atualizar
argumentos_atualizacao = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos_atualizacao.add_argument('id', type=int)
argumentos_atualizacao.add_argument('nome_missao', type=str)
argumentos_atualizacao.add_argument('data_lancamento', type=str)
argumentos_atualizacao.add_argument('destino', type=str)
argumentos_atualizacao.add_argument('estado_missao', type=str)
argumentos_atualizacao.add_argument('tripulacao', type=str)
argumentos_atualizacao.add_argument('carga_util', type=str)
argumentos_atualizacao.add_argument('duracao_missao', type=str)
argumentos_atualizacao.add_argument('custo_missao', type=str)
argumentos_atualizacao.add_argument('status_missao', type=str)

#para deletar
argumentos_exclusao = reqparse.RequestParser()
argumentos_exclusao.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class Cria_missao(Resource):
    def post(self):
        try:
            datas = argumentos_criacao.parse_args()
            Missoes.salva_missao(self,datas['nome_missao'],datas['data_lancamento'],datas['destino'],datas['estado_missao'],datas['tripulacao'],datas['carga_util'],datas['duracao_missao'],datas['custo_missao'],datas['status_missao'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class Atualiza_missao(Resource):
    def put(self):
        try:
            datas = argumentos_atualizacao.parse_args()
            Missoes.atualiza_missoes(self,
            datas['id'], 
            datas['nome_missao'],
            datas['data_lancamento'],
            datas['destino'],
            datas['estado_missao'],
            datas['tripulacao'],
            datas['carga_util'],
            datas['duracao_missao'],
            datas['custo_missao'],
            datas['status_missao']
            )
            return {"message": 'Products update successfully!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class Deleta_missao(Resource):
    def delete(self, id_missao):
        try:
            missao = Missoes.query.get(id_missao)
            if not missao:
                return jsonify({'message': 'Missão não encontrada'}), 404
            missao.delete()
            return jsonify({'message': 'Missão excluída com sucesso!'}), 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
