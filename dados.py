# Gêneros disponíveis para cadastro de livros
GENEROS = (
    "Romance",
    "Ficção",
    "Cordel",
    "Poesia",
    "Didático",
    "Infantil",
    "Biografia",
    "Outros"
)
# Estados de conservação aceitos
estados_conservacao = (
    "Ótimo",
    "Bom",
    "Regular"
)

# Lista que armazenará os livros cadastrados
livros = []

# Conjunto para controlar ISBNs duplicados
isbns_cadastrados = set()

# Código inicial dos livros
proximo_codigo = 1