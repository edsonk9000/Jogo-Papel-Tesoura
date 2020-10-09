print("Jogo Jokenpooo"* 4)
import random

lista = ["papel","tesoura","pedra"]

jogador = input("Escolha entre papel pedra ou tesoura: ")
maquina = random.choice(lista)
if jogador == "pedra" and maquina == "pedra":
    print("Deu empate!!!")
elif jogador == "tesoura" and maquina == "tesoura":
    print("Deu empate!!!")
elif jogador == "papel" and maquina == "papel":
    print("Deu empate!!!")
elif jogador == "pedra" and maquina == "tesoura":
    print("Jogador Ganhou!!!")
elif jogador == "papel" and maquina == "pedra":
     print("Jogador Ganhou!!!")
elif jogador == "tesoura" and maquina == "papel":
     print("Jogador Ganhou!!!")
elif maquina == "pedra" and jogador == "tesoura":
     print("Maquina Ganhou!!!")
elif maquina == "papel" and jogador == "pedra":
      print("Maquina Ganhou!!!")
elif maquina == "tesoura" and jogador == "papel":
      print("Maquina Ganhou!!!")
print(maquina)