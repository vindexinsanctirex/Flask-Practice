from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Olá mundo'

@app.route('/produtos')
def get_produtos():
    produtos = [
        {'id': 1, 'nome': 'Maçã', 'preço': 5.5},
        {'id': 2, 'nome': 'Pêra', 'preço': 7.0}
    ]
    return produtos

tarefas = [
        {'id': 1, 'título': 'Lavar Roupas', 'status': 'pendente', 'categoria': 'domicílio'},
        {'id': 2, 'título': 'Comprar Pão', 'status': 'concluída', 'categoria': 'domicílio'},
        {'id': 3, 'título': 'Preencher Formulários', 'status': 'concluída', 'categoria': 'trabalho'},
        {'id': 4, 'título': 'Passear', 'status': 'pendente', 'categoria': 'lazer'},
        {'id': 5, 'título': 'Formatar HD', 'status': 'pendente', 'categoria': 'trabalho'},
        {'id': 6, 'título': 'Fazer Feira', 'status': 'concluída', 'categoria': 'domicílio'}
    ]

@app.route('/tarefas')
def get_tarefas(): 
    return tarefas

@app.route('/tarefas/status')
def get_status():
    feito = []
    for tarefa in tarefas:
        if tarefa['status'] == 'concluída':
            feito.append(tarefa)
    return feito