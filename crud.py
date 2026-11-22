import dados

from utils import (
    validar_texto,
    validar_isbn,
    validar_preco,
    validar_quantidade
)


def cadastrar_livro():
    """
    Cadastra um novo livro no sistema.
    """
    print("\n--- CADASTRO DE LIVRO ---")

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    isbn = input("Digite o ISBN (13 dígitos): ")

    if not validar_texto(titulo):
        print("Erro: o título não pode ficar vazio.")
        return

    if not validar_texto(autor):
        print("Erro: o autor não pode ficar vazio.")
        return

    if not validar_isbn(isbn):
        print("Erro: o ISBN deve possuir exatamente 13 dígitos.")
        return

    if isbn in dados.isbns_cadastrados:
        print("Erro: este ISBN já está cadastrado.")
        return

    print("\nGêneros disponíveis:")

    for indice, genero in enumerate(dados.GENEROS, start=1):
        print(f"{indice} - {genero}")

    opcao_genero = input("Escolha o gênero do livro: ")

    if not opcao_genero.isdigit():
        print("Erro: escolha uma opção numérica.")
        return

    opcao_genero = int(opcao_genero)

    if opcao_genero < 1 or opcao_genero > len(dados.GENEROS):
        print("Erro: gênero inválido.")
        return

    genero = dados.GENEROS[opcao_genero - 1]

    print("\nEstados de conservação:")

    for indice, estado in enumerate(dados.ESTADOS_CONSERVACAO, start=1):
        print(f"{indice} - {estado}")

    opcao_estado = input("Escolha o estado de conservação: ")

    if not opcao_estado.isdigit():
        print("Erro: escolha uma opção numérica.")
        return

    opcao_estado = int(opcao_estado)

    if opcao_estado < 1 or opcao_estado > len(dados.ESTADOS_CONSERVACAO):
        print("Erro: estado de conservação inválido.")
        return

    estado = dados.ESTADOS_CONSERVACAO[opcao_estado - 1]