

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor


class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            print("erro")

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
            # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total += venda.quantidade * venda.valor
        return total


def main():
    relatorio = Relatorio()

    for i in range(3):
        produto = 'casa' + str(i + 1)
        quantidade = 1 + int( i+ 1)
        valor = 100 + float( i+ 1)
        venda = Venda(produto, quantidade, valor)
        print(venda.produto, venda.quantidade, venda.valor)
        relatorio.adicionar_venda(venda)


    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.

    print(relatorio.calcular_total_vendas())


if __name__ == "__main__":
    main()