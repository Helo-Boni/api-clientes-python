from flask import Flask, request, jsonify

app = Flask(__name__)

clientes = []

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    dados = request.json
    clientes.append(dados)
    return jsonify({"mensagem": "Cliente adicionado!"})

app.run(debug=True)
