from flask import Flask, request, jsonify

app = Flask(__name__)

clientes = []

@app.route('/')
def home():
    return "API de Clientes funcionando 🚀"

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    dados = request.json
    
    if not dados.get("nome") or not dados.get("email"):
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400

    clientes.append(dados)
    return jsonify({"mensagem": "Cliente adicionado!"}), 201

app.run(debug=True)
