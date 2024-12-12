#01. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
def desafio01():
    print("Neste desafio, somarei 2 números inteiros para você")
    while True:
        try:
            n1: int = int(input("Digite o primeiro número inteiro: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2: int = int(input("Digite o segundo número inteiro: "))
        except ValueError:
            continue
        else:
            break
    
    return n1 + n2

#02. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
def desafio02():
    print("Neste desafio, mostrarei o resto da divisão por 5 do número inteiro que você indicar")
    while True:
        try:
            n1: int = int(input("Digite um número inteiro: "))
        except ValueError:
            continue
        else:
            break
    return n1 % 5

#03. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
def desafio03():
    print("Neste desafio, multiplicarei 2 números reais para você")
    while True:
        try:
            n1: float = float(input("Digite o primeiro número real: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2: float = float(input("Digite o segundo número real: "))
        except ValueError:
            continue
        else:
            break
    
    return n1 * n2

#04. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
def desafio04():
    print("Neste desafio, retornarei a divisão inteira do primeiro número inteiro sobre o segundo para você")
    while True:
        try:
            n1: int = int(input("Digite o primeiro número inteiro: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2: int = int(input("Digite o segundo número inteiro: "))
        except ValueError:
            continue
        else:
            if n2 == 0: #não pode ser dividido por 0
                continue
            else:
                break
    
    return n1 // n2

#05. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
def desafio05():
    print("Neste desafio, retornarei a segunda potência de um número inteiro para você.")
    while True:
        try:
            n1: int = int(input("Digite um número inteiro: "))
        except ValueError:
            continue
        else:
            break
        
    return n1 ** 2

#06. Escreva um programa que receba dois números flutuantes e realize sua adição.
def desafio06():
    print("Neste desafio, somarei 2 números reais para você")
    while True:
        try:
            n1: float = float(input("Digite o primeiro número real: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2: float = float(input("Digite o segundo número real: "))
        except ValueError:
            continue
        else:
            break
    
    return n1 + n2

#07. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
def desafio07():
    print("Neste desafio, calcularei a média entre 2 números reais para você")
    while True:
        try:
            n1: float = float(input("Digite o primeiro número real: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2: float = float(input("Digite o segundo número real: "))
        except ValueError:
            continue
        else:
            break
    
    return (n1 + n2)/2

#08. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
def desafio08():
    print("Neste desafio, calcularei a potência da base e do expoente que você fornecer")
    while True:
        try:
            n1: float = float(input("Digite a base (número real): "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2: float = float(input("Digite o expoente (número real): "))
        except ValueError:
            continue
        else:
            break
    
    return n1 ** n2

#09. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
def desafio09():
    print("Neste desafio, converteri a temperatura de graus Celsius para Fahrenhiet")
    while True:
        try:
            n1: float = float(input("Digite a temperatura em graus Celsius (número real): "))
        except ValueError:
            continue
        else:
            break
    
    return f'{n1 * 9/5 + 32} Fahrenheit'

#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
def desafio10():
    print("Neste desafio, calcularei a área do círculo a partir do raio fornecido")
    import math
    while True:
        try:
            n1: float = float(input("Digite o raio do círculo a ser calculado (número real): "))
        except ValueError:
            continue
        else:
            break
    
    return f'área = {n1 ** 2 * math.pi:.2f}'

#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
def desafio11():
    print("Neste desafio, converterei o texto informado em caixa alta (maiúsculas).")    
    n1: str = input("Digite o texto a ser convertido: ")        
    return n1.upper()

#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def desafio12():
    print("Neste desafio, converterei o texto informado em caixa baixa (minúsculas).")    
    n1: str = input("Digite o texto a ser convertido: ")        
    return n1.lower()

#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
def desafio13():
    print("Neste desafio, retirarei do texto informado eventuais espaços no início e no fim.")
    n1: str = input("Digite o texto a ser transformado: ")        
    return n1.strip()

#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
def desafio14():
    print("Neste desafio, dividirei a data entre dia, mês e ano.")
    #while True:
        #try:
        #data = input("Digite uma data em formato dd/mm/yyyy: ")
        #from datetime import datetime
       # data = datetime.strptime(data, "%d/%m;%Y")
        #except 
    data: str = input("Digite uma data em formato dd/mm/yyyy: ")    
    dia: str = data.split('/')[0]
    mes: str = data.split('/')[1]
    ano: str = data.split('/')[2]
    return f'dia: {dia}; mês: {mes}; ano: {ano}'

#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
def desafio15():
    print("Neste desafio, concatenarei dois textos que você me fornecer.")
    texto1: str = input("Digite o primeiro texto: ")
    texto2: str = input("Digite o segundo texto: ")
    return texto1 + texto2

#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def desafio16():
    print("Neste desafio, informarei o resultado da tabela verdade AND das duas variáveis booleanas.")
    while True:
        valor1: str = input("Digite o primeiro valor (True/False): ").upper()
        if valor1 in [0,'F','FALSE','FALSO']:
            valor1: bool = False
            break
        elif valor1 in ['1','T','TRUE','V','VERDADEIRO']:
            valor1: bool = True
            break
    while True:
        valor2: str = input("Digite o segundo  valor (True/False): ").upper()
        if valor2 in ['0','F','FALSE','FALSO']:
            valor2: bool = False
            break
        elif valor2 in [1,'T','TRUE','V','VERDADEIRO']:
            valor2: bool = True
            break
    return f'{valor1} and {valor2} = {valor1 and valor2}'

#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def desafio17():
    print("Neste desafio, informarei o resultado da tabela verdade OR das duas variáveis booleanas.")
    while True:
        valor1: str = input("Digite o primeiro valor (True/False): ").upper()
        if valor1 in ['0','F','FALSE','FALSO']:
            valor1: bool = False
            break
        elif valor1 in ['1','T','TRUE','V','VERDADEIRO']:
            valor1: bool = True
            break
    while True:
        valor2: str = input("Digite o segundo valor (True/False): ").upper()
        if valor2 in ['0','F','FALSE','FALSO']:
            valor2: bool = False
            break
        elif valor2 in ['1','T','TRUE','V','VERDADEIRO']:
            valor2: bool = True
            break
    return f'{valor1} or {valor2} = {valor1 or valor2}'

#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def desafio18():
    print("Neste desafio, informarei o resultado da tabela verdade NOT da variável booleana.")
    while True:
        valor1: str = input("Digite um valor (True/False): ").upper()
        if valor1 in ['0','F','FALSE','FALSO']:
            valor1: bool = False
            break
        elif valor1 in ['1','T','TRUE','V','VERDADEIRO']:
            valor1: bool = True
            break

    resultado = not valor1
    return f'NOT {valor1} = {resultado}'

#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
def desafio19():
    print("Neste desafio, compararei se são iguais as duas entradas de dados.")
    valor1: str = input('Digite a primeira entrada: ')
    valor2: str = input('Digite a segunda entrada: ')
    if valor1 == valor2:
        return f'Os valores "{valor1}" são iguais.'
    else:
        return f'Os valores "{valor1}" e "{valor2}" são diferentes.'

#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
def desafio20():
    print("Neste desafio, compararei se são diferentes as duas entradas de dados.")
    while True:
            try:
                valor1: float = float(input("Digite o primeiro valor: "))
            except ValueError:
                continue
            else:
                break
    while True:
            try:
                valor2: float = float(input("Digite o segundo valor: "))
            except ValueError:
                continue
            else:
                break
    if valor1 != valor2:
        return f'Os valores "{valor1:.2f}" e "{valor2:.2f}" são diferentes.'
    else:
        return f'Os valores "{valor1:.2f}" são iguais.'

#Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a
# entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
def desafio21 ():
    print('Neste desafio converterei a temperatura de Celsius para Fahrenheit.')
    while True:
        try:
            temp_c: float = float(input('Digite a temperatura em Celsius para conversão:'))
            if isinstance(temp_c,float):
                break
        except ValueError:
            print('Você deve digitar um número.')
    return f'{temp_c}º C = {temp_c *9/5 +32}º F'

#Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
def desafio22():
    print('Neste desafio testarei se o texto ou palavra escrita é um palíndromo.')
    teste_palindromo: str = input('Digite a palavra a ser testada: ')
    teste_palindromo: str = teste_palindromo.replace(" ","").lower()
    lista_palindromo: list = list(teste_palindromo)
    lista_reversa: list = lista_palindromo[::-1]
    if lista_palindromo == lista_reversa:
        return f'"{teste_palindromo}" é um palíndromo.'
    else:
        return f'"{teste_palindromo}" NÃO é um palíndromo.'


#Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.
def desafio23():
    print('Neste desafio realizarei uma operação de calculadora básica.')
    while True:
        try:
            n1: float = float(input('Digite o primeiro número: '))
            if isinstance(n1,float):
                break
        except ValueError:
            print('Você deve digitar um número.')
    
    while True:
        operacao: str = input("Digite uma operação (+, -, *, /): ").strip()
        if operacao in ['+', '-', '*', '/']:
            break
        else:
            print('Você deve digitar uma das operações informadas.')

    while True:
        try:
            n2: float = float(input('Digite o segundo número: '))
            if isinstance(n2,float):
                if (operacao == "/" and n2 == 0):
                    print('Não é possível dividir por 0')
                else:
                    break
        except ValueError:
            print('Você deve digitar um número.')
    
    if operacao == "+":
        return f"{n1} + {n2} = {n1+n2}"
    elif operacao == "-":
        return f"{n1} - {n2} = {n1-n2}"
    elif operacao == "*":
        return f"{n1} * {n2} = {n1*n2}"
    elif operacao == "/":
        return f"{n1} / {n2} = {n1/n2}"

#Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else 
# para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".
def desafio24():
    print("Neste desafio, classificarei o número inteiro que você digitar.")
    while True:
        try:
            n1: int = int(input("Digite um número inteiro: "))
        except ValueError:
            continue
        else:
            break
    if n1 > 0:
        tipo_n1: str = 'positivo'
    elif n1 < 0:
        tipo_n1: str = 'negativo'
    else:
        tipo_n1: str = 'neutro'
    if n1 % 2 == 0:
        par_n1: str = 'par'
    else:
        par_n1: str = 'ímpar'
    return f'O número {n1} é {tipo_n1} e {par_n1}.'

#Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que 
# cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
def desafio25():
    print("Neste desafio, tentarei converter uma lista de números separados por vírgula.")
    lista: str = input('Digite uma lista de números separados por vírgula: ')
    lista_separada: list = lista.split(',')
    try:
        for i in lista_separada:
            int(lista_separada[1])
    except ValueError:
        return 'Não foi possível converter sua lista em números'
    else:
        return lista_separada

#Exercício 26: Verificação de Qualidade de Dados
#Você está analisando um conjunto de dados de vendas e precisa garantir que 
#todos os registros tenham valores positivos para quantidade e preço. 
#Escreva um programa que verifique esses campos e imprima "Dados válidos" 
#se ambos forem positivos ou "Dados inválidos" caso contrário.
def desafio26():
    print('Neste desafio, vou registrar a quantidade e preço de compra de um produto.')
    quantidade: str = input('Digite a quantidade comprada: ')
    preco: str = input('Digite o preço do produto comprado: ')
    try:
        if int(quantidade) > 0 and float(preco) > 0:
            return 'Dados válidos'
        else:
            return 'Dados inválidos (valor não positivo)'
    except ValueError:
        return 'Dados inválidos (tipo não numérico)'

#Exercício 27: Classificação de Dados de Sensor
#Imagine que você está trabalhando com dados de sensores IoT. 
#Os dados incluem medições de temperatura. 
#Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'
def desafio27():
    print('Este desafio tem como objetivo avaliar e classificar a temperatura informada.')
    while True:
        try:
            temperatura: float = float(input('Digite a temperatura a ser avaliada em ºC: '))
        except ValueError:
            print('Você precisa digitrar um número...')
        else:
            break
    if temperatura < 18:
        return 'Baixa'
    elif temperatura <= 26:
        return 'Normal'
    else:
        return 'Alta' 

#Exercício 28: Filtragem de Logs por Severidade
#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
def desafio28():
    log = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão remota'},
           {'timestamp': '2024-12-01 21:00:00', 'level': 'OK', 'message': 'Conexão estabelecida'},
           {'timestamp': '2024-12-01 22:00:00', 'level': 'OK', 'message': 'Conexão estabelecida'},
           {'timestamp': '2024-12-01 23:00:00', 'level': 'ERROR', 'message': 'Falha na conexão servidor'}]
    log_erro: dict = {}
    for registro in log:
        if registro['level'] == 'ERROR':
            log_erro[registro['timestamp']] = registro['message']
    
    return log_erro

#Exercício 29: Validação de Dados de Entrada
#Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" 
# ou o erro específico encontrado.
def desafio29():
    print('Neste desafio validarei sua idade e email.')
    while True:
        try:
            idade: int = int(input('Digite sua idade: '))
        except ValueError:
            print('Digite um valor válido...')
        else:
            break
    email: str = input('Digite seu email: ')
    idade_valida: bool = False
    email_valido: bool = False
    if idade >= 18 and idade <= 65:
        idade_valida: bool = True
    if '@' in email: #arrumar para colocar ponto também
        if '.' in email.split('@')[1]: #se tiver '.' após '@'
            email_valido: bool = True

    if idade_valida == True and email_valido == True:
        return f'idade {idade} e email {email} válidos'
    else:
        return 'dados inválidos'
    #elif idade_valida == False and email_valido == False:
    #    return f'idade {idade} e email {email} inválidos'
    #elif idade_valida == False and email_valido == True:
    #    return f'idade {idade} inválida e email {email} válido'
    #elif idade_valida == True and email_valido == False:
    #    return f'idade {idade} válida e email {email} inválido

#Exercício 30: Detecção de Anomalias em Dados de Transações
#Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.
#Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário 
# comercial (antes das 9h ou depois das 18h). Dada uma transação como 
# transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.
def desafio30():
    import random
    lista_transacoes: list = []
    lista_transacoes_suspeitas: list = []
    for i in range(1,21):
        transacao: dict = {}
        transacao['registro'] = i
        transacao['valor'] = random.randint(1,20000)
        transacao['hora'] = random.randint(0,23)
        lista_transacoes.append(transacao) #lista completa
        if (transacao['valor'] > 10000 and (transacao['hora'] > 18 or transacao['hora'] < 9)):
            lista_transacoes_suspeitas.append(transacao) #lista suspeitos
        
    return f'TRANSACOES: {lista_transacoes}\n TRANSACOES SUSPEITAS: {lista_transacoes_suspeitas}'

#Exercício 31: Contagem de Palavras em Textos
# Dado um texto, contar quantas vezes cada palavra única aparece nele.
def desafio31():
    texto: str = input('Digite um texto: ')
    lista_texto: str = texto.replace(',',' ').replace('-',' ').replace('.',' ').split()
    contador_palavras: int = len(lista_texto)
    contador_palavras_diferentes: int = len(set(lista_texto))
    
    return f'       qtd palavras: {contador_palavras} \nqdt palavras diferentes: {contador_palavras_diferentes}'


#Exercício 32. Normalização de Dados
#Normalizar uma lista de números para que fiquem na escala de 0 a 1.
def desafio32():
    print('Neste desafio normalizarei sua lista de números reais.')
    lista: list = []
    lista_normalizada: list = []
    while True:
        try:
            n: str = input("Digite um número real, ou digite '-' para finalizar: ")
            if n == '-':
                break
            else:
                lista.append(float(n))
        except ValueError:
            print('Você deve digitar um número real...')
    for i in lista:
        norm: float = i/max(lista)
        lista_normalizada.append(norm)
    return f'sua lista: {lista} \nlista normalizada: {lista_normalizada}'


#Exercício 33. Filtragem de Dados Faltantes
#Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando.
def desafio33():
    print('Neste desafio vou retornar os registros com campo em branco.')
    from random import choice
    choices: list = ['email@email.com','']
    emails: list[dict] = [{'nome': 'jose','email':choice(choices)},
              {'nome': 'maria','email':choice(choices)},
              {'nome': 'joao','email':choice(choices)},
              {'nome': 'pedro','email':choice(choices)},
              {'nome': 'ana','email':choice(choices)}]
    email_faltante: list = []
    for nome in emails:
        if nome['email'] == '':
            email_faltante.append(nome['nome'])
        
              
    return f' lista de emails: {emails}\n emails faltantes: {email_faltante}'


#Exercício 34. Extração de Subconjuntos de Dados
# Dada uma lista de números, extrair apenas aqueles que são pares.
def desafio34():
    print('Neste desafio vou extrair os números pares do conjunto de dados.')
    from random import randint
    qtd_lista: int = randint(3,10)
    lista: list = []
    lista_pares: list = []
    for i in range(0,qtd_lista):
        numero: int = randint(0,100)
        lista.append(numero)
        if numero % 2 == 0:
            lista_pares.append(numero)
    return f'       lista = {lista}\n lista pares = {lista_pares}'


#Exercício 35. Agregação de Dados por Categoria
#Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
def desafio35():
    print('Neste desafio vou realizar os somatórios agrupados das categorias de vendas.')
    from random import randint
    vendas: list = [
        {"categoria": "eletrônicos", "valor": randint(100,1000)},
        {"categoria": "livros", "valor": randint(100,1000)},
        {"categoria": "eletrônicos", "valor": randint(100,1000)},
        {"categoria": "escritório", "valor": randint(100,1000)},
        {"categoria": "escritório", "valor": randint(100,1000)},
        {"categoria": "eletrônicos", "valor": randint(100,1000)},
        {"categoria": "livros", "valor": randint(100,1000)}]
    agregacao_por_categoria: dict = {}

    for venda in vendas:
        categoria: str = venda['categoria']

        valor: int = venda['valor']
        if categoria in agregacao_por_categoria:
            agregacao_por_categoria[categoria] += valor
        else:
            agregacao_por_categoria[categoria] = valor
    return f'vendas:{vendas}\n{10*'-'}\nvendas por categoria: {agregacao_por_categoria}'

#Exercício 36. Leitura de Dados até Flag
#Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
def desafio36():
    print('Neste desafio vou registrar dados até que você queira sair.')
    lista: list = []
    while True:        
        texto: str = input('Digite uma palavra/número (ou "sair" para finalizar): ')
        if texto == 'sair':
            break
        else:
            lista.append(texto)

    return f'{lista}'

#Exercício 37. Validação de Entrada
#Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
def desafio37():
    print('Neste desafio vou solicitar a entrada de dados até que seja válida.')
    while True:
        try:
            num: int = int(input('Digite um número entre 0 e 10: '))
        except ValueError:
            'você não digitou um número'
        if num >=0 and num <=10:
            break
    return f'você digitou o número {num}.'


#Exercício 38. Consumo de API Simulado
#Simular o consumo de uma API paginada, 
# onde cada "página" de dados é processada em loop até que não haja mais páginas.
def desafio38():
    print('Neste desafio vou imprimir as páginas de uma API para você.')
    from random import randint
    pagina_atual: int = 0
    total_paginas: int = randint(2,10)
    with open('log.txt', 'w') as log:
        while pagina_atual <= total_paginas:
            log.write(f'Processando pg. {pagina_atual} de {total_paginas}\n')
            pagina_atual += 1
    with open('log.txt', 'r') as log:
        conteudo: str = log.read()

    return conteudo
        

#Exercício  39. Tentativas de Conexão
#Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
def desafio39():
    print('Neste desafio vou simular tentativas de conexão até um limite de 5')
    from random import randint
    max_tentativas: int = 5
    tentativa: int = 1
    with open('log.txt', 'w') as log:
        while tentativa <= max_tentativas:
                if randint(1,5) == 5:
                    log.write('Conexão estabelecida')
                    break
                else:
                    log.write(f'Tentativa {tentativa} de {max_tentativas}\n')
                tentativa += 1
        else:
            log.write(f'Falha na conexão após {max_tentativas} tentativas.')

    with open('log.txt', 'r') as log:
        conteudo: str = log.read()
                
    return conteudo

#Exercício 40. Processamento de Dados com Condição de Parada
#Processar itens de uma lista até encontrar um valor específico que indica a parada.
def desafio40():
    from random import choice
    lista: list = []
    for i in range(0,10):
        if 'parar' in lista:
            break
        else:
            lista.append(choice(['parar',i,i,i,i]))
    with open('log.txt', 'w') as log:
        i: int = 1
        while i < len(lista):
            if lista[i] == 'parar':
                log.write('Parada encontrada, encerrando processamento.')
                break
            else:
                log.write(f'Processando item {i} de {len(lista)}.\n')
            i +=1

    with open('log.txt', 'r') as log:
        conteudo: str = log.read()
    return lista,conteudo

menu = """MENU DE DESAFIOS
#01. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#02. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#03. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#04. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#05. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#06. Escreva um programa que receba dois números flutuantes e realize sua adição.
#07. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#08. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#09. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#21. Faça um programa que converta a temperatura de Celsius para Fahrenheitcom checagem de erro.
#22. Faça um detector de palíndromo.
#23. Faça uma calculadora simples.
#24. Classifique um número intenro em (positivo/negativo/neutro) e (par/ímpar).
#25. Converta uma lista de números de string para lista.
#26. Verificação de Qualidade de Dados
#27. Classificação de Dados de Sensor
#28. Filtragem de Logs por Severidade
#29: Validação de Dados de Entrada
#30: Detecção de Anomalias em Dados de Transações
#31: Contagem de Palavras em Textos
#32. Normalização de Dados
#33. Filtragem de Dados Faltantes
#34. Extração de Subconjuntos de Dados
#35. Agregação de Dados por Categoria
#36. Leitura de Dados até Flag
#37. Validação de Entrada
#38. Consumo de API Simulado
#39. Tentativas de Conexão
#40. Processamento de Dados com Condição de Parada
#41. SAIR
"""



def main():
    while True:
        print(menu)
        desafio: None = None
        while desafio not in range(1,41):
            try:
                desafio: int = int(input("Escolha o desafio de 1 a 40 (41 para sair): \n"))
            except ValueError:
                continue
        
        
        print(10*"*=*")
        print("Você escolheu o desafio ",desafio,"!")

        desafios: dict = {
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
        13: desafio13,
        14: desafio14,
        15: desafio15,
        16: desafio16,
        17: desafio17,
        18: desafio18,
        19: desafio19,
        20: desafio20,
        21: desafio21,
        22: desafio22,
        23: desafio23,
        24: desafio24,
        25: desafio25,
        26: desafio26,
        27: desafio27,
        28: desafio28,
        29: desafio29,
        30: desafio30,
        31: desafio31,
        32: desafio32,
        33: desafio33,
        34: desafio34,
        35: desafio35,
        36: desafio36,
        37: desafio37,
        38: desafio38,
        39: desafio39,
        40: desafio40}
        


        resultado = desafios[desafio]()

        print(8*"~=~","RESULTADO",8*"~=~")
        try:
            print(f'{resultado:^59}')
        except TypeError:
            print (resultado)
        print(59*"=")
        resposta: None = None
        while resposta not in ['y','yes','yep','n','not','nope']:
            resposta: str = input('Gostaria de abrir outro desafio? [y/n]: ').lower()
        if resposta in ['n','nope','not','nao','não']:
            break

if __name__ == "__main__":
    main()
