#01. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
def desafio01():
    print("Neste desafio, somarei 2 números inteiros para você")
    while True:
        try:
            n1 = int(input("Digite o primeiro número inteiro: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2 = int(input("Digite o segundo número inteiro: "))
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
            n1 = int(input("Digite um número inteiro: "))
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
            n1 = float(input("Digite o primeiro número real: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            n2 = float(input("Digite o segundo número real: "))
        except ValueError:
            continue
        else:
            break
    
    return n1 * n2

#04. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
def desafio04():
    return None

#05. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
def desafio05():
    return None

#06. Escreva um programa que receba dois números flutuantes e realize sua adição.
def desafio06():
    return None

#07. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
def desafio07():
    return None

#08. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
def desafio08():
    return None

#09. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
def desafio09():
    return None

#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
def desafio10():
    return None

#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
def desafio11():
    return None

#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def desafio12():
    return None

#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
def desafio13():
    return None

#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
def desafio14():
    return None

#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
def desafio15():
    return None

#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def desafio16():
    return None

#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def desafio17():
    return None

#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def desafio18():
    return None

#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
def desafio19():
    return None

#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
def desafio20():
    return None


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
#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes."""




def main():
    while True:
        print(menu)
        desafio = None
        while desafio not in range(1,21):
            try:
                desafio = int(input("Escolha o desafio de 1 a 20: \n"))
            except ValueError:
                continue
        
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
        13: desafio13,
        14: desafio14,
        15: desafio15,
        16: desafio16,
        17: desafio17,
        18: desafio18,
        19: desafio19,
        20: desafio20}

        resultado = desafios[desafio]()

        print(4*"~=~","RESULTADO",4*"~=~")
        print(f'{resultado:^33}')
        print(7*"~=~=~")
        resposta = None
        while resposta not in ['y','yes','yep','n','not','nope']:
            resposta = input('Gostaria de abrir outro desafio? [y/n]: ')
            if resposta in ['n','nope','not']:
                break

if __name__ == "__main__":
    main()
