import math

Presente_OBJ = [
        {"ID": 1, "AREA": (5, 5,5)},
        {"ID": 2, "AREA": (6, 6,6)},
        {"ID": 3, "AREA": (7, 7,7)},
        {"ID": 4, "AREA": (102, 15,166)},
        {"ID": 5, "AREA": (150, 5,126)},
    ]
for i in Presente_OBJ:
    print(i["ID"], math.prod(i["AREA"]))

num_test_cases = int(input("Informe o número de casos de teste: "))  # Número de casos de teste

for _ in range(num_test_cases):

    num_presents_to_choose = int(input(
        "Informe o número de presentes que Bruninho deseja escolher: "))  # K: Quantidade de presentes que Bruninho quer
    total_presents = 0  # N: Total de presentes disponíveis

    # Lista para armazenar os presentes
    present_list = []

    for i in Presente_OBJ:
        present_list.append((i["ID"], math.prod(i["AREA"])))
        total_presents +=1

    print(present_list)

    # Ordena os presentes: primeiro por volume (decrescente), depois por ID (crescente)
    present_list.sort(key=lambda x: (-x[1], x[0]))

    print(present_list)

    # Seleciona os K primeiros presentes e imprime os IDs em ordem lexicográfica
    # -x[1]) será ordenado de forma decrescente (por isso o sinal negativo).
    #x[0]) será ordenado de forma crescente (padrão) se houver empates no primeiro critério.


    # usa uma list comprehension para criar uma nova lista com os primeiros elementos de cada tupla
    selected_presents = [present[0] for present in present_list[:num_presents_to_choose]]
    selected_presents.sort()
    print("IDs dos presentes selecionados:", *selected_presents)
