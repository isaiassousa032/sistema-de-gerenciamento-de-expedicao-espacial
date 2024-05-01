class Missao:
    def __init__(self, id, nome_da_missao, data_de_lancamento, destino, estado, tripulacao, duracao, status, carga_util ) -> None:
        self.id = id
        self.nome_da_missao = nome_da_missao
        self.data_de_lancamento = data_de_lancamento
        self.destino = destino
        self.estado = estado
        self.tripulacao = tripulacao
        self.duracao = duracao
        self.status = status
        self.carga_util = carga_util

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome_da_missao": self.nome_da_missao,
            "data da lançamento": self.data_de_lancamento,
            "destino": self.destino,
            "estado": self.estado,
            "tripulação": self.tripulacao,
            "duração": self.duracao,
            "status": self.status,
            "carga util": self.carga_util
        }