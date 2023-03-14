from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'É assim que acaba',
        'autor': 'Colleen Hoover'
    },

    {
        'id': 2,
        'titulo': 'Um caso perdido',
        'autor': 'Colleen Hoover'
    },

    {
        'id': 3,
        'titulo': 'Sem esperança',
        'autor': 'Colleen Hoover'
    },

    {
        'id': 4,
        'titulo': 'É assim que começa',
        'autor': 'Colleen Hoover'
    }
]

#CONSULTAR (TODOS)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#CONSULTAR(ID)
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#EDITAR 
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#CRIAR
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#EXCLUIR
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
    
app.run(port=5000, host='localhost', debug=True)