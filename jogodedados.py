import random

sair= False
while sair==False:
        
    print("simulador de dados!")
    print("Jogue dois dados. Se o resultado for par a máquina vence, impar você vence!")
    n1= random.randint(1,6)
    print(f"O resultado do primeiro dado é {n1}")
    n2= random.randint(1,6)
    print(f"O resultado do segundo dado é {n2}")
    resul=n1+n2
    print(f"O resultado final é {resul}")
    if resul %2==0:
        print("Resultado par, a máquina venceu!")
    else:
        print("Resultado impar, parabéns, você venceu!")
            
    teste = input("Pressione 's' para sair ou ENTER para jogar novamente  ")
    if teste == "s":
        sair = True

