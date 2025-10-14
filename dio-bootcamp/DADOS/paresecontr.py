def findNumOfPairs(a, b):
    a.sort()
    b.sort()

    contador = 0
    position = 0

    for i in range(len(a)):
        # Procurar o primeiro b[position] que é maior que a[i]
        while position < len(b) and b[position] <= a[i]:
            position += 1

        if position < len(b):
            contador += 1
            position += 1  # Passa para o próximo elemento de b

    return contador


# Testando a função
a = [1, 2, 3]
b = [1, 2, 1]
resultado = findNumOfPairs(a, b)
print(f"Resultado: {resultado}")
