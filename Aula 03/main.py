from flask import Flask, jsonify, request
from models import db, Produto
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


with app.app_context():
    db.create_all()


produtos = [
    {
        "id": 1,
        "nome": "Smartphone",
        "preco": 1500.50,
        "categoria": "Eletrônicos"
    },
    {
        "id": 2,
        "nome": "Notebook",
        "preco": 3200.00,
        "categoria": "Eletrônicos"
    },
    {
        "id": 3,
        "nome": "Camiseta",
        "preco": 55.99,
        "categoria": "Vestuário"
    },
    {
        "id": 4,
        "nome": "Livro de Ficção",
        "preco": 35.75,
        "categoria": "Livros"
    }
]

@app.route('/produtos')
def get_produtos():
    return produtos

@app.route('/teste-db')
def test_banco():
    return {'mensagem': 'Banco estável'}


if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/produtos/<int:produto_id>', methods=['PUT'])
# def atualizar_produto(produto_id):
#     dados = request.json

#     for prod in produtos:
#         if prod['id'] == produto_id:
#             prod['nome'] = dados.get('nome', prod['nome'])
#             prod['preco'] = dados.get('preco', prod['preco'])
#             prod['categoria'] = dados.get('categoria', prod['categoria'])

#             return jsonify({
#                 'mensagem': 'Produto atualizado com sucesso',
#                 'produto': prod
#             }), 200
#     return jsonify({'erro': 'Produto não encontrado'}), 404

# @app.route('/produtos/<int:produto_id>', methods=['DELETE'])
# def reomver_produto(produto_id):

#     for prod in produtos:
#         if prod['id'] == produto_id:
#             prod['status'] = 'inativo'
#             return jsonify({
#                 'mensagem': 'Produto removido com sucesso' #remoção fake
#             }), 200







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


# app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///tarefas.db'

# db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()

# class Tarefa:
#     id = db.Column(db.Integer, primary_key=True)
#     título = db.Column(db.String(100), nullable=False)


# tarefas = [
#     {
#         "id": 1,
#         "título": "Tarefa: Exercício físico",
#         "status": "concluída"
#     },
# {
#         "id": 2,
#         "título": "Tarefa: Exercício do curso",
#         "status": "pendente"
#     },
# {
#         "id": 3,
#         "título": "Tarefa: Alimentar o cachorro",
#         "status": "concluída"
#     },
# {
#         "id": 4,
#         "título": "Tarefa: Correr na praia",
#         "status": "pendente"
#     },
#     {
#         "id": 5,
#         "título": "Tarefa: Completar o código",
#         "status": "concluída"
#     },
# ]

# @app.route('/tarefas') #essencial pra fazer o API funcionar, o GET inicial.
# def get_dados():
#     return tarefas

# @app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
# def atualizar_tarefa(tarefa_id):
#     dados = request.json

#     if not dados['título']:
#         return jsonify({'mensagem': 'Título não encontrado'}), 400

#     for taref in tarefas:
#         if taref['id'] == tarefa_id:
#             taref['título'] = dados.get('título', taref['título'])
#             taref['status'] = dados.get('status', taref['status'])

#             return jsonify({
#                 'mensagem': 'Tarefa atualizada com sucesso',
#                 'produto': taref
#             }), 200
#     return jsonify({'erro': 'Tarefa não encontrada'}), 404

# @app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
# def remover_tarefa(tarefa_id):

#     for taref in tarefas:
#         if taref['id'] == tarefa_id:
#             tarefas.remove(taref)
#             return jsonify({
#                 'mensagem': 'Tarefa removida com sucesso' #remoção verídica
#             }), 200
        
#     return jsonify({'erro': 'Tarefa não encontrada'}), 404



# @app.route('/tarefas/<int:tarefa_id>')
# def get_tarefa(tarefa_id):
#     for taref in tarefas:
#         if taref['id'] == tarefa_id:
#             return taref
#     return jsonify({'erro': 'Tarefa não encontrada'}), 404

# @app.route('/tarefas')
# def get_products():
#     # Obter parâmetros de consulta da URL
#     status = request.args.get('status')

#     resultados = tarefas

#     # Filtrar por status
#     if status:
#         resultados = [t for t in resultados if t['status'].lower() == status.lower()]
    
#     return jsonify(resultados)

# @app.route('/tarefas', methods=['POST'])
# def criar_tarefas():
#     dados = request.json


#     if not dados.get('título') or not dados.get('status'):
#         return jsonify({'erro': 'Dados Incompletos'}), 400

#     if dados.get('título') == '':
#         return jsonify({'erro': 'O nome não pode estar em branco'}), 400

#     # novo_produto ={
#     #     'id': 10,
#     #     'nome': dados['nome'],
#     #     'preco'
#     # }
#     tarefas.append(dados)
#     print(tarefas)
#     return jsonify({'mensagem': 'Tarefa Cadastrada'}), 201