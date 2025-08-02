from flask import Flask, jsonify, request

app = Flask(__name__)

# produtos = [
#     {
#         "id": 1,
#         "nome": "Smartphone",
#         "preco": 1500.50,
#         "categoria": "Eletrônicos"
#     },
#     {
#         "id": 2,
#         "nome": "Notebook",
#         "preco": 3200.00,
#         "categoria": "Eletrônicos"
#     },
#     {
#         "id": 3,
#         "nome": "Camiseta",
#         "preco": 55.99,
#         "categoria": "Vestuário"
#     },
#     {
#         "id": 4,
#         "nome": "Livro de Ficção",
#         "preco": 35.75,
#         "categoria": "Livros"
#     }
# ]

# # Exemplo de como aceder a um elemento:
# # print(produtos[0]["nome"]) # Para aceder ao nome do primeiro produto
# # print(produtos[2]["preco"]) # Para aceder ao preço do terceiro produto

# @app.route('/produtos')
# def get_products():
#     # Obter parâmetros de consulta da URL
#     categoria = request.args.get('categoria')
#     preco_max = request.args.get('preco_max')
#     preco_min = request.args.get('preco_min')

#     resultados = produtos

#     # Filtrar por categoria
#     if categoria:
#         resultados = [p for p in resultados if p['categoria'].lower() == categoria.lower()]

#     # Filtrar por preço máximo
#     if preco_max:
#         try:
#             preco_max_float = float(preco_max)
#             resultados = [p for p in resultados if p['preco'] <= preco_max_float]
#         except ValueError:
#             return jsonify({"erro": "Parâmetro 'preco_max' inválido"}), 400

#     # Filtrar por preço mínimo
#     if preco_min:
#         try:
#             preco_min_float = float(preco_min)
#             resultados = [p for p in resultados if p['preco'] >= preco_min_float]
#         except ValueError:
#             return jsonify({"erro": "Parâmetro 'preco_min' inválido"}), 400

#     return jsonify(resultados)

# @app.route('/produtos', methods=['POST'])
# def criar_produtos():
#     dados = request.json


#     if not dados.get('nome') or not dados.get('preco'):
#         return jsonify({'erro': 'Dados Incompletos'}), 400

#     if dados.get('nome') == '':
#         return jsonify({'erro': 'O nome não pode estar em branco'}), 400

#     # novo_produto ={
#     #     'id': 10,
#     #     'nome': dados['nome'],
#     #     'preco'
#     # }
#     produtos.append(dados)
#     print(produtos)
#     return jsonify({'mensagem': 'Produto Cadastrado'}), 201


tarefas = [
    {
        "id": 1,
        "título": "Tarefa: Exercício físico",
        "status": "concluída"
    },
{
        "id": 2,
        "título": "Tarefa: Exercício do curso",
        "status": "pendente"
    },
{
        "id": 3,
        "título": "Tarefa: Alimentar o cachorro",
        "status": "concluída"
    },
{
        "id": 4,
        "título": "Tarefa: Correr na praia",
        "status": "pendente"
    },
    {
        "id": 5,
        "título": "Tarefa: Completar o código",
        "status": "concluída"
    },
]


@app.route('/tarefas/<int:tarefa_id>')
def get_tarefa(tarefa_id):
    for taref in tarefas:
        if taref['id'] == tarefa_id:
            return taref
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tarefas')
def get_products():
    # Obter parâmetros de consulta da URL
    status = request.args.get('status')

    resultados = tarefas

    # Filtrar por status
    if status:
        resultados = [t for t in resultados if t['status'].lower() == status.lower()]
    
    return jsonify(resultados)

@app.route('/tarefas', methods=['POST'])
def criar_tarefas():
    dados = request.json


    if not dados.get('título') or not dados.get('status'):
        return jsonify({'erro': 'Dados Incompletos'}), 400

    if dados.get('título') == '':
        return jsonify({'erro': 'O nome não pode estar em branco'}), 400

    # novo_produto ={
    #     'id': 10,
    #     'nome': dados['nome'],
    #     'preco'
    # }
    tarefas.append(dados)
    print(tarefas)
    return jsonify({'mensagem': 'Tarefa Cadastrada'}), 201