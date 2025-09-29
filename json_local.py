import json
import os

# Nome do arquivo que vamos criar
NOME_ARQUIVO = "alunos.json"

def salvar_dados(dados):
    """Salva uma lista de dicionários em um arquivo JSON."""
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            # json.dump() escreve os dados no arquivo
            # indent=4 formata o arquivo para ser mais legível
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"✅ Dados salvos com sucesso no arquivo '{NOME_ARQUIVO}'!")
    except IOError as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")

def ler_dados():
    """Lê e exibe os dados de um arquivo JSON."""
    # Verifica se o arquivo existe antes de tentar lê-lo
    if not os.path.exists(NOME_ARQUIVO):
        print(f"⚠️  O arquivo '{NOME_ARQUIVO}' ainda não existe. Execute o salvamento primeiro.")
        return None

    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
            # json.load() carrega os dados do arquivo para uma variável Python
            dados = json.load(f)
        print(f"\n--- Dados lidos do arquivo '{NOME_ARQUIVO}' ---")
        # Imprime os dados de forma legível
        for item in dados:
            print(item)
        return dados
    except (IOError, json.JSONDecodeError) as e:
        print(f"❌ Erro ao ler ou decodificar o arquivo: {e}")
        return None

if __name__ == "__main__":
    # 1. Definimos os dados iniciais dos alunos
    alunos_para_salvar = [
        {"nome": "Renan G Santos", "curso": "Análise e Desenvolvimento de Sistemas"},
        {"nome": "Maheus Zoreck", "curso": "Ciência da Computação"},
        {"nome": "Kleber Lima", "curso": "Análise e Desenvolvimento de Sistemas"}
    ]

    # 2. Chamamos a função para salvar os dados no arquivo
    salvar_dados(alunos_para_salvar)

    # 3. Chamamos a função para ler os dados do arquivo e exibi-los
    ler_dados()