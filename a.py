import random


palavras = ["macaco", "banana", "aleatorio", "mclovin", "alexandre de morais"]

def jogo_adivinhacao():
    sorteio =  random.choice(palavras)
    tentativas = 0
    certas = ["_" for _ in sorteio]

    print(f"A palavra tem {len(sorteio)} letras.")

    while True:
        chute = input("Adivinhe uma letra ou digite 'sair' para encerrar: ").lower()

        if chute == "sair":
            print(f"Você desistiu. A palavra era: {sorteio}.")
            break
    
        if len(chute) == 1 and chute.isalpha():
            tentativas += 1

            if chute in sorteio:
                for i, letra in enumerate(sorteio):
                    if letra == chute:
                        certas[i] = letra
                print(f"Letras corretas até agora: {' '.join(certas)}")
            else:
                print(f"A letra '{chute}' não está na palavra.")
            
            if "_" not in certas:
                print(f"Parabéns! Você acertou a palavra '{sorteio}' em {tentativas} tentativas.")
                break
        else:
            print("Digite algo válido")

jogo_adivinhacao()
