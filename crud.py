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

    for indice, estado in enumerate(dados.estados_conservacao, start=1):
        print(f"{indice} - {estado}")

    opcao_estado = input("Escolha o estado de conservação: ")

    if not opcao_estado.isdigit():
        print("Erro: escolha uma opção numérica.")
        return

    opcao_estado = int(opcao_estado)

    if opcao_estado < 1 or opcao_estado > len(dados.estados_conservacao):
        print("Erro: estado de conservação inválido.")
        return

    estado = dados.estados_conservacao[opcao_estado - 1] 
    
    try:
        preco = float(input("Digite o preço do livro: R$ "))

    except ValueError:
        print("Erro: digite um preço válido.")
        return

    if not validar_preco(preco):
        print("Erro: o preço deve ser maior que zero.")
        return

    try:
        quantidade = int(input("Digite a quantidade de livros: "))

    except ValueError:
        print("Erro: digite uma quantidade válida.")
        return

    if not validar_quantidade(quantidade):
        print("Erro: a quantidade não pode ser negativa.")
        return

    codigo = dados.proximo_codigo

    livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "genero": genero,
        "estado": estado,
        "preco": preco,
        "quantidade": quantidade
    }

    dados.livros.append(livro)
    dados.isbns_cadastrados.add(isbn)
    dados.proximo_codigo += 1

    print("\nLivro cadastrado com sucesso!")
    print(f"Código do livro: {codigo}")

    
def listar_livros():
    """
    Exibe todos os livros cadastrados no sistema.
    """
    print("\n--- LISTA DE LIVROS ---")

    if not dados.livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in dados.livros:
        print("-------------------------")
        print(f"Código: {livro['codigo']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Conservação: {livro['estado']}")
        print(f"Preço: R$ {livro['preco']:.2f}")
        print(f"Quantidade: {livro['quantidade']}")

def buscar_livro():
    """
    Busca um livro pelo título ou ISBN.
    """
    print("\n--- BUSCAR LIVRO ---")

    busca = input("Digite o título ou ISBN do livro: ").strip().lower()

    if not busca:
        print("Erro: digite alguma informação para buscar.")
        return

    encontrados = [
        livro for livro in dados.livros
        if busca in livro["titulo"].lower()
        or busca == livro["isbn"]
    ]

    if not encontrados:
        print("Nenhum livro encontrado.")
        return

    for livro in encontrados:
        print("-------------------------")
        print(f"Código: {livro['codigo']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Conservação: {livro['estado']}")
        print(f"Preço: R$ {livro['preco']:.2f}")
        print(f"Quantidade: {livro['quantidade']}")