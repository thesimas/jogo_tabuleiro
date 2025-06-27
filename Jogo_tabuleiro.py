import random
print("\n")
print('Bem vindo ao jogo de Tabuleiro em Python!\n')

nome_jogador_1 = input('Olá, me informe o nome do primeiro jogador:  ')
nome_jogador_2 = input('Olá, me informe o nome do segundo jogador:  ')
print("\n")
print('Agora, iremos definir quem irá jogar primeiro!\n')

#Definindo quem irá começar jogando o jogo!
while True: 
    jogar_dado = input(f'{nome_jogador_1}, aperte "Enter" para jogar o dado: \n')

    while jogar_dado != "":
        print("Comando inválido, apenas aperte 'Enter'.\n")
        jogar_dado = input(f'{nome_jogador_1}, Tente novamente: \n')
        if jogar_dado == "":
            break
        else:
            continue
    if jogar_dado == "":
        dado_jogador_1 = random.randrange(1,6 + 1)
        print(f'O/A dado do/a {nome_jogador_1} caiu com o valor {dado_jogador_1}!\n')
        jogar_dado = input(f'Agora o/a {nome_jogador_2} irá jogar o dado, aperte "Enter" para jogar o dado: \n')
    while jogar_dado != "":
        print("Comando inválido, apenas aperte 'Enter'.\n")
        jogar_dado = input(f'{nome_jogador_2}, Tente novamente: \n')
        if jogar_dado == "":
            break
        else:
            continue
    if jogar_dado == "":
            dado_jogador_2 = random.randrange(1,6 + 1)
            print(f'O/A dado do/a {nome_jogador_2}, caiu com o valor {dado_jogador_2}!\n')
    if dado_jogador_1 > dado_jogador_2:
        print(f'O/A {nome_jogador_1} irá começar o jogo!\n')
        primeiro_jogador = nome_jogador_1
        segundo_jogador = nome_jogador_2
        break
        
    elif dado_jogador_1 == dado_jogador_2:
        print(f'Os dados de vocês cairam iguais, terão que jogar uma nova rodada!\n')
        continue
    else:
        print(f'O/A {nome_jogador_2} irá começar o jogo!\n')
        primeiro_jogador = nome_jogador_2
        segundo_jogador = nome_jogador_1
        break

#Marcando a posição de cada jogador.
lista_jogador_1 = ['_'] * 20 
posicao_atual_1 = 0
lista_jogador_1[posicao_atual_1] = "X"
lista_jogador_2 = ['_'] * 20
posicao_atual_2 = 0
lista_jogador_2[posicao_atual_2] = "X"

contador_rodadas = 0
#Desenvolvendo o jogo!
print(f'{primeiro_jogador} você está aqui:{' '*10}{'  '.join(lista_jogador_1)}\n') #Mostrando para o usuario aonde ele está. Metodo .join, remove o colchete e as virgulas.
while True:
    contador_rodadas += 1 
    if contador_rodadas > 1: 
        print(f"{primeiro_jogador} você está aqui:{' '*10}{'  ' .join(lista_jogador_1)}  e chegou sua vez de jogar!\n")
    jogar_dado = input(f'{primeiro_jogador}, aperte "Enter" para jogar o dado: \n')
    while jogar_dado != "":
        print("Comando inválido, apenas aperte 'Enter'.\n")
        jogar_dado = input(f'{primeiro_jogador}, Tente novamente: \n')
        if jogar_dado == "":
            break
        else:
            continue
    if jogar_dado == "":
        dado_jogador_1 = random.randrange(1,6 + 1)
        print(f'O dado do/a {primeiro_jogador} caiu com o valor {dado_jogador_1}!\n')
        print(f'Para você avançar {dado_jogador_1} casas, você terá que acertar a pergunta a seguir!\n')

        numero_1 = random.randint(1,10)
        numero_2 = random.randint(1,10)
        lista_perguntas = [f"Qual é a Tabuada de {numero_1} x {numero_2}?\n"]
        while True:
            try:
                resposta = int(input(" ".join(lista_perguntas)))
                break
            except ValueError:
                print("Tipo de várivel errada, informe um número inteiro para a resposta da sua pergunta!")

        if resposta == numero_1 * numero_2:
            if posicao_atual_1 + dado_jogador_1 >= 20: 
                posicao_antiga_1 = posicao_atual_1
                posicao_nova_1 = posicao_antiga_1 + dado_jogador_1
                lista_jogador_1[posicao_antiga_1] = "_"
                lista_jogador_1[19] = "X"
                posicao_atual_1 = posicao_nova_1

                print(f'Parabéns {nome_jogador_1}, você acertou a pergunta e chegou na ultima posição!\n{'  '.join(lista_jogador_1)}\n')
                break
            else:
            #lógica para mover a posição do jogador
                posicao_antiga_1 = posicao_atual_1 
                posicao_nova_1 = posicao_atual_1 + dado_jogador_1 
                lista_jogador_1[posicao_antiga_1] = "_"
                lista_jogador_1[posicao_nova_1] = "X"
                posicao_atual_1 = posicao_nova_1

                print(f'Parabéns, {primeiro_jogador} acertou a pergunta e avançou {dado_jogador_1} casas!\n')
                print(f"{primeiro_jogador} você está aqui:{' '*10}{'  ' .join(lista_jogador_1)}\n") 

        else: 
            print(f'{primeiro_jogador} errou a questão e permaneceu na mesma casa!\n{primeiro_jogador}, você está aqui: {'  ' .join(lista_jogador_1)}\n')
    if posicao_atual_1 >= 19:
        break
    print(f"{segundo_jogador} você está aqui:{' '*10}{'  ' .join(lista_jogador_2)}  e chegou sua vez de jogar!\n")

    jogar_dado = input(f'{segundo_jogador}, aperte "Enter" para jogar o dado: \n')
    while jogar_dado != "":
        print("Comando inválido, apenas aperte 'Enter'.\n")
        jogar_dado = input(f'{segundo_jogador}, Tente novamente: \n')
        if jogar_dado == "":
            break
        else:
            continue
    if jogar_dado == "":
        dado_jogador_2 = random.randrange(1,6 + 1)
        print(f'O dado do/a {segundo_jogador} caiu com o valor {dado_jogador_2}!\n')
        print(f'Para você avançar {dado_jogador_2} casas, você terá que acertar a pergunta a seguir!\n')

        numero_1 = random.randint(1,10)
        numero_2 = random.randint(1,10)
        lista_perguntas = [f"Qual é a Tabuada de {numero_1} x {numero_2}?\n"]

        while True:
            try:
                resposta = int(input(" ".join(lista_perguntas)))
                break
            except ValueError:
                print("Tipo de várivel errada, informe um número inteiro para a resposta da sua pergunta!")
        
        if resposta == numero_1 * numero_2:
            if posicao_atual_2 + dado_jogador_2 >= 20:
                posicao_antiga_2 = posicao_atual_2
                posicao_nova_2 = posicao_antiga_2 + dado_jogador_2
                lista_jogador_2[posicao_antiga_2] = "_"
                lista_jogador_2[19] = "X"
                posicao_atual_2 = posicao_nova_2
                print(f'Parabéns, {nome_jogador_2} você acertou a pergunta e chegou na ultima posição!\n{'  ' .join(lista_jogador_2)}\n')
                break
            else:
                posicao_antiga_2 = posicao_atual_2 
                posicao_nova_2 = posicao_atual_2 + dado_jogador_2 
                lista_jogador_2[posicao_antiga_2] = "_"
                lista_jogador_2[posicao_nova_2] = "X" 
                posicao_atual_2 = posicao_nova_2

                print(f'Parabéns, {segundo_jogador} acertou a pergunta e avançou {dado_jogador_2} casas!\n')
                print(f"{segundo_jogador} você está aqui:{' '*10}{'  ' .join(lista_jogador_2)}\n") 
        else: 
            print(f'{segundo_jogador} errou a questão e permaneça na mesma casa!\n{segundo_jogador}, você está aqui: {'  ' .join(lista_jogador_2)}\n')

        if posicao_atual_2 >= 19:
            break
        
if posicao_atual_1 >= 19:
    print(f"Parabéns {primeiro_jogador} você ganhou o jogo!\n")

else:
    print(f"Parabéns {segundo_jogador} você ganhou o jogo!\n")

print("Jogo desenvolvido por: Luciano Simas Junior | 1° fase de ADS |\n")