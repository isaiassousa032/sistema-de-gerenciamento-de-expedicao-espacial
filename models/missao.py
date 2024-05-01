class Missao:
    def __init__(self,id, nome, data_de_lancamento, destino, estado, tripulacao, duracao, status ) -> None:
        self.id = id
        self.nome = nome
        self.data_de_lancamento = data_de_lancamento
        self.destino = destino
        self.estado = estado
        self.tripulacao = tripulacao
        self.duracao = duracao
        self.status = status

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data da lançamento": self.data_de_lancamento,
            "destino": self.destino,
            "estado": self.estado,
            "tripulação": self.tripulacao,
            "duração": self.duracao,
            "status": self.status
        }