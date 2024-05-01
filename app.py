from flask import Flask 
from models.missao import Missao

# Cria uma nova instância da classe Flask, atribuindo-a à variável app
# o __name__ tem valor __main__
app = Flask(__name__) 

missoes = []


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=2961) 