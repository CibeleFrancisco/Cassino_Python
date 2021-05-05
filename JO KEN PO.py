"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""
import random
user = int(input("""Escolha entre as opções: 
1 - pedra
2 - papel
3 - tesoura:  """))
if user ==1:
    print(f'Você escolheu pedra')
elif user ==2:
    print("Você escolheu papel")
elif user ==3:
    print("Você escolheu tesousa")
else:
    print("\33[7:31:40mValor inválido!\33[m")
comp = random.randint(1,3)
if comp==1:
    print("O Computador escolheu pedra")
elif comp==2:
    print("O computador escolheu papel")
elif comp==3:
    print("O computador escolheu tesoura")
if user ==comp:
    print("Empate!")
elif user == 3 and comp ==1:
    print("Computador venceu!")
elif user ==1 and comp ==3:
    print("Você venceu!")
elif user < comp:
    print("Você venceu!!")
elif comp < user:
    print("Computador venceu")