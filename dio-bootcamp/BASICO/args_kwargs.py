def show_poem(data_ext, *args, **kwargs):
    # Função que recebe três tipos de argumentos:
    # 1. 'data_ext': um argumento obrigatório (string) que pode ser o título ou data do poema.
    # 2. '*args': argumentos posicionais variáveis que serão usados para as linhas do poema.
    # 3. '**kwargs': argumentos nomeados variáveis usados para os metadados do poema (autor, ano, etc.).

    text = "\n".join(args)
    # Cria uma string 'text' onde cada elemento em 'args' (as linhas do poema)
    # é unido por quebras de linha ('\n'). Se não houver nenhum argumento em 'args', 'text' será vazio.

    meta_dados = '\n'.join([f"{key.title()}: {valor}" for key, valor in kwargs.items()])
    # Cria uma string 'meta_dados' onde cada par chave-valor dos argumentos nomeados ('kwargs')
    # é formatado como "Chave: Valor", onde a chave é capitalizada (primeira letra maiúscula).
    # Os pares chave-valor são unidos por quebras de linha ('\n'). Se 'kwargs' estiver vazio, 'meta_dados' será vazio.

    message = f"{data_ext}\n\n{text}\n\n{meta_dados}"
    # Cria a string 'message' que combina:
    # - 'data_ext' no topo, seguido por duas quebras de linha.
    # - 'text' (o poema) abaixo de 'data_ext', seguido por duas quebras de linha.
    # - 'meta_dados' (os metadados como autor e ano) no final.
    # Se algum desses elementos ('text' ou 'meta_dados') estiver vazio, apenas não será exibido conteúdo naquela parte.

    print(message)
    # Exibe a mensagem final no console.


# Exemplo de uso da função:
show_poem("sexta dia 23/11/2024","zen of python", "beautiful is better than ugly.", autor="Tim ertes", ano=1999)
# Chama a função 'show_poem' com:
# - 'data_ext' sendo "zen of python".
# - Uma linha do poema passada como argumento posicional: "beautiful is better than ugly.".
# - Dois metadados passados como argumentos nomeados: 'autor' sendo "Tim ertes" e 'ano' sendo 1999.
