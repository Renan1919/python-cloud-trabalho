from flask import Flask, jsonify
import json

# Inicializa a aplicação Flask
app = Flask(__name__)


# --- Base de Dados (carregada do arquivo JSON) ---
def carregar_alunos():
    """Carrega os dados dos alunos do arquivo alunos.json."""
    try:
        with open('alunos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Retorna uma lista vazia se o arquivo não existir ou for inválido
        return []


# --- Definição das Rotas da API ---

# Rota 1: Raiz (/)
# Apenas uma mensagem de boas-vindas para testar se a API está no ar.
@app.route("/")
def home():
    """Rota principal que exibe uma mensagem de boas-vindas."""
    return "<h1>API de Alunos está no ar!</h1><p>Use as rotas /alunos, /saudacao/&lt;nome&gt; ou /curso/&lt;curso&gt;</p>"


# Rota 2: Lista de Alunos (/alunos)
# Retorna a lista completa de alunos em formato JSON.
@app.route("/alunos")
def get_alunos():
    """Retorna a lista completa de alunos do arquivo JSON."""
    alunos = carregar_alunos()
    return jsonify(alunos)


# Rota 3: Saudação Dinâmica (/saudacao/<nome>)
# Uma rota que recebe um nome como parâmetro e devolve uma saudação.
@app.route("/saudacao/<string:nome>")
def saudacao(nome):
    """Retorna uma saudação personalizada em JSON."""
    return jsonify({"mensagem": f"Olá, {nome}! Bem-vindo(a) à nossa API."})


# Rota 4: Filtrar Alunos por Curso (/curso/<curso>)
# Rota dinâmica que filtra e retorna alunos com base no curso fornecido.
@app.route("/curso/<string:curso>")
def get_alunos_por_curso(curso):
    """Filtra e retorna alunos que pertencem a um curso específico."""
    alunos = carregar_alunos()
    # A "List Comprehension" abaixo filtra a lista de alunos
    alunos_filtrados = [aluno for aluno in alunos if aluno.get("curso").lower() == curso.lower()]

    if not alunos_filtrados:
        return jsonify({"erro": f"Nenhum aluno encontrado para o curso: {curso}"}), 404

    return jsonify(alunos_filtrados)


# --- Execução do Servidor ---
if __name__ == "__main__":
    # O app.run() inicia o servidor web.
    # debug=True faz com que o servidor reinicie automaticamente após cada alteração no código.
    app.run(debug=True)

