#1. Crie um dicionário para armazenar informações de um livro,
# incluindo Título, autor e ano de publicação. Imprima cada informação
def desafio01():
    from typing import Dict, Any
    
    livro:Dict[str, Any] = {
        "Título": "Bíblia",
        "Autor": "Vários",
        "Ano": -4000}
    return livro




#2. Preço total da lista de compras
def desafio02():
    from typing import Dict, Any

    lista_compras = ["maçã", "banana", "cereja"]
    precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
    return None


#3. Eliminação de Duplicatas 
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
def desafio03():
    emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
    return None

#4. Filtragem de Dados
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
def desafio04():
    idades = [22, 15, 30, 17, 18]
    return None
#5. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
def desafio05():

    pessoas = [
        {"nome": "Alice", "idade": 30},
        {"nome": "Bob", "idade": 25},
        {"nome": "Carol", "idade": 20}]
    return None

#6. Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.
def desafio06():

    numeros = [10, 20, 30, 40, 50]
    return None

#7. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
def desafio07():

    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return None

#8. Atualização de Dados
#Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
def desafio08():

    produtos = [
        {"id": 1, "nome": "Teclado", "preço": 100},
        {"id": 2, "nome": "Mouse", "preço": 80},
        {"id": 3, "nome": "Monitor", "preço": 300}
    ]
    return None

# Atualizar o preço do produto com id 2 para 90

#9. Fusão de Dicionários
#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
def desafio09():

    dicionario1 = {"a": 1, "b": 2}
    dicionario2 = {"c": 3, "d": 4}

    return None

#10. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
def desafio10():

    estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
    return None
#11. Extração de Chaves e Valores
#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
def desafio11():

    dicionario = {"a": 1, "b": 2, "c": 3}
    return None

#12. Contagem de Frequência de Itens
#Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
def desafio12():

    texto = "engenharia de dados"
    return None


menu = """MENU DE DESAFIOS
#01. Dicionário de livros.
#02. Preço total da lista de compras.
#03. Eliminação de Duplicatas.
#04. Filtragem de Dados.
#05. Ordenação Personalizada.
#06. Agregação de Dados.
#07. Divisão de Dados em Grupos
#08. Atualização de Dados
#09. Fusão de Dicionários
#10. Filtragem de Dados em Dicionário
#11. Extração de Chaves e Valores
#12. Contagem de Frequência de Itens
# 13. SAIR
"""



def main():
    while True:
        print(menu)
        desafio = None
        while desafio not in range(1,13):
            try:
                desafio = int(input("Escolha o desafio de 1 a 12 (13 para sair): \n"))
            except ValueError:
                continue
        
        
        print(10*"*=*")
        print("Você escolheu o desafio ",desafio,"!")

        desafios = {
        1: desafio01,
        2: desafio02,
        3: desafio03,
        4: desafio04,
        5: desafio05,
        6: desafio06,
        7: desafio07,
        8: desafio08,
        9: desafio09,
        10: desafio10,
        11: desafio11,
        12: desafio12,
        }
        


        resultado = desafios[desafio]()

        print(8*"~=~","RESULTADO",8*"~=~")
        try:
            print(f'{resultado:^59}')
        except TypeError:
            print (resultado)
        print(59*"=")
        resposta = None
        while resposta not in ['y','yes','yep','n','not','nope']:
            resposta = input('Gostaria de abrir outro desafio? [y/n]: ').lower()
        if resposta in ['n','nope','not','nao','não']:
            break

if __name__ == "__main__":
    main()
