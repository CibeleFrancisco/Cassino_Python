import random

sair= False
while sair==False:

    print("Jogo da SORTE! teste sua sorte")
    print("Tente advinhar o número entre 1 e 100")
    print("Se acertar o número ganhe 100% do prêmio")
    print("Se acertar a dezena correspondente ganhe 20% do prêmio")
    print("Se acertar 2 números anteriores ou posteriores ganhe 25% do prêmio")
    repetir= False
    while repetir== False:
        
        x= int(input("Digite um número entre 1 e 100: "))
               
        if x not in range (1,100):
            print("número inválido!")
            repetir=False
        else:
            repetir = True
            
    y= random.randint(1,100)

    decimalx= x//10%100
    decimaly= y//10%100

    if decimalx==decimaly:
      print(f"Número sorteado {y}")
      print("PARABÉNS, VOCÊ GANHOU 20% DO PRÊMIO")

    elif x-1 ==y:
        print(f"Número sorteado {y}")
        print("PARABÉNS, VOCÊ GANHOU 25% DO PRÊMIO")

    elif x-2 ==y:
        print(f"Número sorteado {y}")
        print("PARABÉNS, VOCÊ GANHOU 25% DO PRÊMIO")

    elif x+1 ==y:
        print(f"Número sorteado {y}")
        print("PARABÉNS, VOCÊ GANHOU 25% DO PRÊMIO")

    elif x+2 ==y:
        print(f"Número sorteado {y}")
        print("PARABÉNS, VOCÊ GANHOU 25% DO PRÊMIO")

    elif x ==y:
        print(f"número sorteado {y}. PARABÉNS, VOCÊ VENCEU!")

    else:
        print(f"Número sorteado {y}")
        print("Você perdeu")

    teste = input("Pressione 's' para sair ou ENTER para jogar novamente  ")
    if teste == "s":
        sair = True
