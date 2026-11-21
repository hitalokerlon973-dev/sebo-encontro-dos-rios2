def validar_texto(texto):
    """
    Verifica se um texto foi preenchido corretamente.
    """
    return texto.strip() != ""


def validar_isbn(isbn):
    """
    Verifica se o ISBN possui exatamente 13 dígitos.
    """
    return isbn.isdigit() and len(isbn) == 13


def validar_preco(preco):
    """
    Verifica se o preço é maior que zero.
    """
    return preco > 0


def validar_quantidade(quantidade):
    """
    Verifica se a quantidade não é negativa.
    """
    return quantidade >= 0