from flask import Flask, jsonify, request
from models import db, Tarefa, Usuario
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


with app.app_context():
    db.create_all()
    
    if Usuario.query.count() == 0:
        usuarios = [
            Usuario(nome='José', email='joseba@tom.com'),
            Usuario(nome='Maria', email='mared@tom.com'),
            Usuario(nome='Cane', email='canesg@gr.com')
        ]
        
        db.session.add_all(usuarios)
        db.session.commit()
    
    if Tarefa.query.count() == 0:
        exemplos = [
            Tarefa(titulo='Estudar Flask', descricao='Criar projeto', status='pendente', user_id=1),
            Tarefa(titulo='Autenticação', descricao='Adicionar login básico', status='concluida', user_id=2),
            Tarefa(titulo='Estudar banco de dados', descricao='', status='pendente', user_id=1),
            Tarefa(titulo='Empilhar estoque', descricao='Organizar inventório', status='concluida', user_id=3)
        ]
        
        db.session.add_all(exemplos)
        db.session.commit()



tarefas = [
    {
        "id": 1,
        "titulo": "Tarefa: Exercício físico",
        "status": "concluída"
    },
{
        "id": 2,
        "titulo": "Tarefa: Exercício do curso",
        "status": "pendente"
    },
{
        "id": 3,
        "titulo": "Tarefa: Alimentar o cachorro",
        "status": "concluída"
    },
{
        "id": 4,
        "titulo": "Tarefa: Correr na praia",
        "status": "pendente"
    },
    {
        "id": 5,
        "titulo": "Tarefa: Completar o código",
        "status": "concluída"
    },
]

@app.route('/tarefas')
def get_tarefas():
    status = request.args.get('status')
    
    if status:
        if status != 'pendente' or status != 'concluida':
            return jsonify({'error': 'Status Inválido!'}), 400
     
        tarefas = Tarefa.query.filter_by(status=status).all()
    else:
        tarefas = Tarefa.query.all()
    
    # tarefas = Tarefa.query.all()
    lista_tarefas = []
    
    for tarefa in tarefas:
        lista_tarefas.append({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status
        })
    return jsonify(lista_tarefas)

@app.route('/usuarios')
def get_usuario():
    
    usuarios = Usuario.query.all()
    lista_usuarios = []
    
    for usuario in usuarios:
        lista_usuarios.append({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email
        })
    return jsonify(lista_usuarios)
    
    

@app.route('/tarefas-usuario')
def get_tarefas_usuario():
    user_id = request.args.get('user_id')
    
    if user_id:
        tarefas = Tarefa.query.filter_by(user_id=user_id).all()
    else:
        tarefas = Tarefa.query.all()
        
    if not user_id:
        return jsonify({'error': 'Usuário não encontrado!'}), 404
    
    # tarefas = Tarefa.query.all()
    lista_tarefas = []
    
    for tarefa in tarefas:
        lista_tarefas.append({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status,
            'user_id': tarefa.user_id
        })
    return jsonify(lista_tarefas)
    
@app.route('/teste-db')
def test_banco():
    return {'mensagem': 'Banco estável'}

@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    dados = request.json
    
    if not dados or not dados['titulo']:
        return jsonify({'error': 'Dados inválidos!'}), 400
    
    nova_tarefa = Tarefa(
        titulo=dados.get('titulo'),
        descricao=dados.get('descricao'),
        status=dados.get('status')
    )
    
    db.session.add(nova_tarefa)
    db.session.commit()
    
    return jsonify({'mensagem': 'Tarefa criada com sucesso!'}), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def update_tarefa(id):
    update_tarefa = request.json
    if not update_tarefa:
        return jsonify({'error': 'Dados inválidos'}), 400
    tarefa = Tarefa.query.get(id)
    
    if not tarefa:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    tarefa.titulo = update_tarefa.get('titulo', tarefa.titulo)
    tarefa.descricao = update_tarefa.get('descricao', tarefa.descricao)
    tarefa.status = update_tarefa.get('status', tarefa.status)
    
    db.session.commit()
    
    return jsonify({
        'mensagem': 'Tarefa atualizada com sucesso'
    })
    
@app.route('/usuarios/<int:id>', methods=["DELETE"])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    
    tarefas = Tarefa.query.filter_by(user_id=id).all()
    
    if tarefas:
        return jsonify({'error': 'O usuário tem tarefas em andamento, não é possível excluir!'})
    
    db.session.delete(usuario)
    db.session.commit()
    
    return jsonify({'mensagem': 'Usuário removido com sucesso!'}), 200

@app.route('/tarefas/<int:id>', methods=["DELETE"])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    
    if not tarefa:
        return jsonify({'error': 'Tarefa não encontrada'}), 400
    
    db.session.delete(tarefa)
    db.session.commit()
    
    return jsonify({'mensagem': 'Tarefa removida com sucesso!'}), 200

@app.route('/tarefas/<int:id>')
def get_tarefa(id):
    tarefa = Tarefa.query.get(id)
    
    if not tarefa:
        return jsonify({
            'erro': 'Tarefa não encontrada'
        }), 404
        
    return jsonify({
        'id': tarefa.id,
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'status': tarefa.status
    })
    
# @app.route('/tarefas/<int:id>', methods=['PUT'])
# def atualizar_tarefa(id):
#     dados = request.json

#     for taref in tarefas:
#         if taref['id'] == id:
#             taref['titulo'] = dados.get('titulo', taref['titulo'])
#             taref['status'] = dados.get('status', taref['status'])
#             taref['descricao'] = dados.get('descricao', taref['descricao'])
#             taref['categoria'] = dados.get('categoria', taref['categoria'])

#             return jsonify({
#                 'mensagem': 'Tarefa atualizada com sucesso',
#                 'tarefa': taref
#             }), 200
            
#     return jsonify({'erro': 'Tarefa não encontrada'}), 404


if __name__ == '__main__':
    app.run(debug=True)