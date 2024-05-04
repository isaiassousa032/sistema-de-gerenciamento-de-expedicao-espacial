
class Missao:
    def __init__(self, id: int, nome_da_missao: str, data_de_lancamento, destino: str, tripulacao: str, duracao, status_da_missao: str, carga_util: str ) -> None:
        self.id = id
        self.nome_da_missao = nome_da_missao
        self.data_de_lancamento = data_de_lancamento
        self.destino = destino
        self.tripulacao = tripulacao
        self.duracao = duracao
        self.status = status_da_missao
        self.carga_util = carga_util

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome_da_missao": self.nome_da_missao,
            "data da lancamento": self.data_de_lancamento,
            "destino": self.destino,
            "tripulacao": self.tripulacao,
            "duracao": self.duracao,
            "status_da_missao": self.status,
            "carga util": self.carga_util
        }