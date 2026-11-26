import json
import os

CAMINHO_ARQUIVO = "dados/livros.json"


def salvar_livros(livros):
    os.makedirs("dados", exist_ok=True)

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)


def carregar_livros():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)