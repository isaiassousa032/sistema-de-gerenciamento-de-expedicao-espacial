from flask import Flask, render_template ##jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
#db = SQLAlchemy()

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
from app.models.missoes import Missoes
with app.app_context():
    db.create_all()

from app.view.reso_missoes import Index, Cria_missao, Atualiza_missao, Deleta_missao
api.add_resource(Index, '/')
api.add_resource(Cria_missao, '/criar')
api.add_resource(Atualiza_missao, '/atualizar')
api.add_resource(Deleta_missao, '/deletar')