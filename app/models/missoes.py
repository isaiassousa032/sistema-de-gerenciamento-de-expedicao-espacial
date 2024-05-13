from app import db
#from decimal import Decimal
#from datetime import date

class Missoes(db.Model):
    __tablename__ = 'missoes'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True) #nullable aceita valores nulos ou não.
    nome_missao = db.Column(db.String(80), nullable=True, unique=True)
    data_lancamento = db.Column(db.DateTime, nullable=False)
    destino = db.Column(db.String(150), nullable=False)
    estado_missao = db.Column(db.String(20), nullable=False)
    tripulacao = db.Column(db.String(300), nullable=False)  
    carga_util = db.Column(db.String(300), nullable=False)
    duracao_missao = db.Column(db.DateTime, nullable=False)  
    custo_missao = db.Column(db.Numeric(10, 2), nullable=False) # Até 10 dígitos com os ultimos dois decimais.
    status_missao = db.Column(db.Text, nullable=False)


    def __init__(self, id, nome_missao, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, custo_missao, status_missao) -> None:
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
    

def cria_missao(self, nome_missao, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, custo_missao, status_missao):
    try:
        nova_missao = Missoes(nome_missao, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, custo_missao, status_missao)
        db.session.add(nova_missao)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao criar missão: {e}")

def ler_todas_missoes(self) -> list[Missoes]:
    try:
        missoes = db.session.query(Missoes).all()
        return missoes
    except Exception as e:
        print(f"Erro ao recuperar todas as missões: {e}")
        return []
    
def ler_missao_por_id(self, id_missao: int) -> Missoes:
    try:
        missao = db.session.query(Missoes).filter(Missoes.id == id_missao).one()
        return missao
    except Exception as e:
        print(f"Erro ao recuperar a missão {id_missao}: {e}")
        return None

def atualiza_missao(self, nome_missao, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, custo_missao, status_missao):
    try:
        db.session.query(Missoes).filter(Missoes.id==id).update({"nome_missao":nome_missao,"data_lancamento": data_lancamento,"destino":destino,"estado_missao":estado_missao,"tripulacao":tripulacao,"carga_util":carga_util,"duracao_missao":duracao_missao,"custo_missao":custo_missao,"status_missao":status_missao})
    except Exception as e:
        print(e)

def deleta_missao(self, id ):
    try:
        db.session.query(Missoes).filter(Missoes.id==id).delete()
        db.session.commit()
    except Exception as e:
        print(f"Erro ao deletar missão {e}")

        
