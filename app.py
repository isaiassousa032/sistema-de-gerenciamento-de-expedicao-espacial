from flask import Flask 

# Cria uma nova instância da classe Flask, atribuindo-a à variável app
# o __name__ tem valor __main__
app = Flask(__name__) 


@app.route("/")
def hello_world(): #trocar para o contexto do projeto posteriormente
    return "Hello world!"

if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=2961) 