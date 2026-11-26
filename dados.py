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

# Carrega os livros salvos no JSON
from arquivo import carregar_livros

livros = carregar_livros()

# Conjunto para controlar ISBNs duplicados
isbns_cadastrados = {
    livro["isbn"] for livro in livros
}

# Próximo código disponível
proximo_codigo = max(
    (livro["codigo"] for livro in livros),
    default=0
) + 1
