from datetime import date
from unicodedata import numeric
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missoes import Missoes

#para criar
argumentos_criacao = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos_criacao.add_argument('id', type=int)
argumentos_criacao.add_argument('nome_missao', type=str, required=True)
argumentos_criacao.add_argument('data_lancamento', type=date)
argumentos_criacao.add_argument('destino', type=str)
argumentos_criacao.add_argument('estado_missao', type=str)
argumentos_criacao.add_argument('tripulacao', type=str)
argumentos_criacao.add_argument('carga_util', type=str)
argumentos_criacao.add_argument('duracao_missao', type=date)
argumentos_criacao.add_argument('custo_missao', type=numeric)
argumentos_criacao.add_argument('status', type=str)

#para ler
argumentos_leitura = reqparse.RequestParser()
argumentos_leitura.add_argument('id', type=int)
argumentos_leitura.add_argument('nome_missao', type=str)
argumentos_leitura.add_argument('data_lancamento', type=date)
argumentos_leitura.add_argument('destino', type=str)
argumentos_leitura.add_argument('estado_missao', type=str)
argumentos_leitura.add_argument('tripulacao', type=str)
argumentos_leitura.add_argument('carga_util', type=str)
argumentos_leitura.add_argument('duracao_missao', type=date)
argumentos_leitura.add_argument('custo_missao', type=numeric)
argumentos_leitura.add_argument('status', type=str)

#para atualizar
argumentos_atualizacao = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos_atualizacao.add_argument('id', type=int)
argumentos_atualizacao.add_argument('nome_missao', type=str)
argumentos_atualizacao.add_argument('data_lancamento', type=date)
argumentos_atualizacao.add_argument('destino', type=str)
argumentos_atualizacao.add_argument('estado_missao', type=str)
argumentos_atualizacao.add_argument('tripulacao', type=str)
argumentos_atualizacao.add_argument('carga_util', type=str)
argumentos_atualizacao.add_argument('duracao_missao', type=date)
argumentos_atualizacao.add_argument('custo_missao', type=numeric)
argumentos_atualizacao.add_argument('status', type=str)

#para deletar
argumentos_exclusao = reqparse.RequestParser()
argumentos_exclusao.add_argument('id', type=int)
'''argumentos_exclusao.add_argument('nome_missao', type=str)
argumentos_exclusao.add_argument('data_lancamento', type=date)
argumentos_exclusao.add_argument('destino', type=str)
argumentos_exclusao.add_argument('estado_missao', type=str)
argumentos_exclusao.add_argument('tripulacao', type=str)
argumentos_exclusao.add_argument('carga_util', type=str)
argumentos_exclusao.add_argument('duracao_missao', type=date)
argumentos_exclusao.add_argument('custo_missao', type=numeric)
argumentos_exclusao.add_argument('status', type=str)'''

class Cria_missao(Resource):
    def post(self):
        try:
            datas = argumentos_criacao.parse_args()
            Missoes.cria_missao(self, datas['id'], datas['nome_missao'],datas['data_lancamento'],datas['destino'],datas['estado_missao'],datas['tripulacao'],datas['carga_util'],datas['duracao_missao'],datas['custo_missao'],datas['status'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class Ler_todas_missoes(Resource):
    def get(self, id_missao):
        try:
            datas = argumentos_leitura.query.get(id_missao)
            if datas:
                return jsonify(datas.serialize()), 200
            else:
                return jsonify({'message': 'Missão não encontrada'}), 404
        except Exception as e:
            return({'Não foi possível ler as missões': f'{e}'}), 500

class Atualiza_missao(Resource):
    def put(self):
        try:
            datas = argumentos_atualizacao.parse_args()
            Missoes.atualiza_missao(self, datas['id'], 
            datas['name'],
            datas['price'],
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
