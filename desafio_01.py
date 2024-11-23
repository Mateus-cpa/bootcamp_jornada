# Cálculo de Bônus com entrada de usuário
#solicitar ao usuário que insira seu nome.
while True:
    nome_usuario = input("Digite seu nome: ")
    if (nome_usuario in ['',' ','.'] or len(nome_usuario)<2):
        print("Digite um nome válido...")
        continue
    elif (nome_usuario.isdigit() or nome_usuario.isnumeric() or nome_usuario.isspace()):
        print("Digite um nome válido...")
        continue
    else:
        break

#inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
while True:
    try: 
        salario_usuario = input("Digite seu salário: ")
        salario_usuario = salario_usuario.replace(",",".")
        salario_usuario = float(salario_usuario)
        if isinstance(salario_usuario,float):
            break
    except TypeError as e:
        print(f'{e}, você não digitou um valor numérico')
    except ValueError as e:
        print(f'{e}, você não digitou um valor numérico')
   

#solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
while True:
    try:
        bonus_usuario = input("Digite o bônus recebido: ")
        bonus_usuario = bonus_usuario.replace(",",".")
        bonus_usuario = float(bonus_usuario)
        if isinstance(bonus_usuario,float):
            break
    except TypeError as e:
        print(f'{e}, você não digitou um valor numérico')
    except ValueError as e:
        print(f'{e}, você não digitou um valor numérico')
    

#calcular do KPI do bônus de 2024 é de 1000 + salario * bônus
kpi = round(1000 + salario_usuario * bonus_usuario,2)

#imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(15*"=","RESULTADO","="*15)
print(f"Olá, {nome_usuario}! \n O seu valor de bônus foi de R$ {kpi:.2f}, \n correspondendo R$ 1000.00 somado ao \n bônus de {bonus_usuario:.2f} sobre o salário R$ {salario_usuario:.2f}.")
print("="*40)