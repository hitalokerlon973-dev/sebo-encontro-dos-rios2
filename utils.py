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