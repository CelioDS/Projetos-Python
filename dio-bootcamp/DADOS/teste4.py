# A classe Venda representa uma venda de um produto.
class Venda:
    def __init__(self, produto, quantidade, valor):
        # Inicializa os atributos da venda: produto, quantidade e valor
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor


# A classe Categoria representa uma categoria de produtos.
class Categoria:
    def __init__(self, nome):
        # Inicializa a categoria com um nome e uma lista vazia de vendas
        self.nome = nome
        self.vendas = []

    # Método para adicionar uma venda à lista de vendas da categoria
    def adicionar_venda(self, venda):
        # Verifica se o parâmetro passado é uma instância da classe Venda
        if isinstance(venda, Venda):
            self.vendas.append(venda)  # Adiciona a venda à lista
        else:
            print("ERRO")  # Se não for uma venda, exibe um erro

    # Método para calcular o total das vendas de uma categoria
    def total_vendas(self):
        total = 0  # Inicializa o total como zero
        for venda in self.vendas:
            total += venda.valor  # Soma o valor de cada venda
        return total  # Retorna o total acumulado


# Função principal para executar o programa
def main():
    categorias = []  # Lista que vai armazenar as categorias

    # Loop para criar duas categorias
    for i in range(3):
        nome_categoria = 'categoria' + str(i + 1)  # Nome da categoria (exemplo: categoria1, categoria2)
        categoria = Categoria(nome_categoria)  # Cria uma nova categoria

        # Loop para adicionar duas vendas a cada categoria
        for j in range(2):
            # A entrada de vendas é uma string, separada por vírgulas
            entrada_venda = f'Produto{i+1}, {2 + int(i + 1)} , {200 + float(i + 1)}'  # Exemplo de entrada de venda: Produto1, 2, 100
            # Separa a string pelos separadores ',' e limpa os espaços em branco
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())  # Converte a quantidade para inteiro
            valor = float(valor.strip())  # Converte o valor para float

            # Cria uma instância da classe Venda
            venda = Venda(produto.strip(), quantidade, valor)

            # Adiciona a venda à categoria usando o método adicionar_venda
            categoria.adicionar_venda(venda)

        # Adiciona a categoria à lista de categorias
        categorias.append(categoria)

    # Exibe o total de vendas para cada categoria
    for categoria in categorias:
        # Chama o método total_vendas para cada categoria e imprime o resultado
        print(f'Vendas em {categoria.nome}: {categoria.total_vendas()}')

# Chama a função main para executar o código
if __name__ == "__main__":
    main()
