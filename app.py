from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
    'id': 1,
    'titulo': 'O Senhor dos Aneis -  A Sociedade do Anel',
    'autor': 'J.R.R. Tolkien'
  },
  {
    'id': 2,
    'titulo': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K. Howling'
  },
  {
    'id': 3,
    'titulo': 'Habitos Atomicos',
    'autor': 'James Clear'
  },
]

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
  for livro in livros:
    # if livro.get('id') == id:
    #   return jsonify(livro)
    if livro['id'] == id:
      return jsonify(livro), 200, {'Content-Type': 'application/json; charset=utf-8'}
    
#Incluir um novo livro
@app.route('/livros', methods=['POST'])
def incluir_livro():
  novo_livro = request.get_json()
  livros.append(novo_livro)

  return jsonify(livros)

#Editar(id)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
  livro_alterado = request.get_json()
  for indice,livro in enumerate(livros):
    if livro['id'] == id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

#Deletar
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
  for indice,livro in enumerate(livros):
    if livro['id'] == id:
      del livros[indice]
  
  return jsonify(livros)