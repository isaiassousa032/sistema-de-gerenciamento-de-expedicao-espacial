
from decimal import Decimal

class Missao:
    def __init__(self, id: int, nome_missao: str, data_lancamento, destino: str, estado_missao: str, tripulacao: str, carga_util: str, duracao_missao: str, custo_missao: str, status_missao: str) -> None:
        self.id = id
        self.nome_missao = nome_missao
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.estado_missao = estado_missao
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao_missao = duracao_missao
        self.custo_missao = custo_missao
        self.status_missao = status_missao
        

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome_missao": self.nome_missao,
            "data_lancamento": self.data_lancamento,
            "destino": self.destino,
            "estado_missao": self.estado_missao,
            "tripulacao": self.tripulacao,
            "carga_util": self.carga_util,
            "duracao_missao": self.duracao_missao,
            "custo_missao": self.custo_missao,
            "status_missao": self.status_missao
        }