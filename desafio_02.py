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

menu = """#01. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
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

desafio = None
print(menu)
while desafio not in range(1,21):
    try:
            desafio = int(input("Escolha a atividade: \n"))
    except ValueError:
        continue


desafio = 'desafio'+str(desafio)
print(desafio)
