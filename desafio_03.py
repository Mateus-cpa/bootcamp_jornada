#1. Crie um dicionário para armazenar informações de um livro,
# incluindo Título, autor e ano de publicação. Imprima cada informação
def desafio01():
    from typing import Dict, Any
    print('Neste desafio retornarei um dicionário de livros ')
    from random import randint

    livros:list[Dict] = [{"Título": "Bíblia",
        "Autor": "Vários",
        "Ano": -4000},
        {"Título": "Odisseia",
        "Autor": "Homero",
        "Ano": -700},
        {"Título": "Ilíada",
        "Autor": "Homero",
        "Ano": -800},
        {"Título": "A República",
        "Autor": "Platão",
        "Ano": -380},
        {"Título": "Alcorão",
        "Autor": "Maomé",
        "Ano": 800},
        {"Título": "Divina Comédia",
        "Autor": "Dante Alighieri",
        "Ano": 1321},
        {"Título": "Do Cativeiro Babilônico da Igreja",
        "Autor": "Martinho Lutero",
        "Ano": 1520}]
    
    return f'Livro selecionado: {livros[randint(0,6)]}'




#2. Preço total da lista de compras
def desafio02():
    from typing import Dict, Any
    print('Neste desafio ')
    lista_compras = ["maçã", "banana", "cereja"]
    precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
    soma = 0
    for valor in precos.values():
        soma += valor

    return f'O total das compras {precos} = {soma}'


#3. Eliminação de Duplicatas 
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
def desafio03():
    print('Neste desafio retirarei duplicatas da lista de emails')
    emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
    emails_sem_duplicatas = set(emails)
    n_total_emails = len(emails)
    n_emails_unicos = len(emails_sem_duplicatas)
    return f'A listagem sem duplicatas é {emails_sem_duplicatas} ({n_emails_unicos} do total de {n_total_emails})'

#4. Filtragem de Dados
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
def desafio04():
    print('Neste desafio gerarei uma lista de idades e separarei apenas os maiores ou iguais a 18.')
    from random import randint    
    idades = []
    for i in range (0,8):
        idades.append(randint(1,60))
    maiores_de_idade = []
    for idade in idades:
        if idade >=18:
            maiores_de_idade.append(idade)
    return f'{maiores_de_idade} são maiores de idade da lista {idades}'

#5. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
def desafio05():
    print('Neste desafio ordenarei os nomes pela idade.')
    from random import randint
    pessoas = [
        {"nome": "Mateus", "idade": randint(4,65)},
        {"nome": "Rejane", "idade": randint(4,65)},
        {"nome": "Mel", "idade": randint(4,65)},
        {"nome": "Ian", "idade": randint(4,65)},
        {"nome": "Alice", "idade": randint(4,65)},
        {"nome": "Bob", "idade": randint(4,65)},
        {"nome": "Carol", "idade": randint(4,65)}]
    pessoas_ordenadas = sorted(pessoas, key=lambda registro: registro['idade'])    
    return pessoas_ordenadas # retorna cada item em uma linha


#6. Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.
def desafio06():
    print('Neste desafio calcularei a média de números aleatórios')
    from random import randint
    numeros = [randint(5,50), randint(5,50), randint(5,50), randint(5,50), randint(5,50)]   
    return f'Números: {numeros}\n Média: {sum(numeros)/len(numeros)}'

#7. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
def desafio07():
    print('Neste desafio repararei os números pares ou ímpares.')
    from random import randint
    valores = []
    for i in range(0,9):
        valores.append(randint (-10,10))
    pares = []
    impares = []
    for n in valores:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return f'Valores: {valores}\n  Pares: {pares}\nÍmpares: {impares}'

#8. Atualização de Dados
#Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
def desafio08():
    from random import randint
    print('Neste desafio atualizarei o preço de um produto para 200.')
    produtos = [
        {"id": 1, "nome": "Teclado", "preço": 100},
        {"id": 2, "nome": "Mouse", "preço": 80},
        {"id": 3, "nome": "Monitor", "preço": 300}
    ]
    from copy import deepcopy
    produtos_alterados = deepcopy(produtos)
    produtos_alterados[randint(0,2)]['preço'] = 200
    return f'{produtos}\n{produtos_alterados}'

# Atualizar o preço do produto com id 2 para 90

#9. Fusão de Dicionários
#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
def desafio09():
    print('Neste desafio ')
    dicionario1 = {"a": 1, "b": 2}
    dicionario2 = {"c": 3, "d": 4}

    return None

#10. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
def desafio10():
    print('Neste desafio ')
    estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
    return None
#11. Extração de Chaves e Valores
#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
def desafio11():
    print('Neste desafio ')
    dicionario = {"a": 1, "b": 2, "c": 3}
    return None

#12. Contagem de Frequência de Itens
#Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
def desafio12():
    print('Neste desafio ')
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
