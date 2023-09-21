# Pedra, Papel, Tesoura
#
#

# 01 - Instancias as variáveis

import random

player = input("Escolhe uma opção: ")
pc = random.choice(("Pedra", "Papel", "Tesoura"))

# 02 - Lógica

if player == "Pedra" and pc == "Pedra":
    resultado = "Jogador Empatou"
if player == "Pedra" and pc == "Papel":
    resultado = "Jogador Perdeu"
if player == "Pedra" and pc == "Tesoura":
    resultado = "Jogador Ganhou"

if player == "Papel" and pc == "Pedra":
    resultado = "Jogador Ganhou"
if player == "Papel" and pc == "Papel":
    resultado = "Jogador Empatou"
if player == "Papel" and pc == "Tesoura":
    resultado = "Jogador Perdeu"

if player == "Tesoura" and pc == "Pedra":
    resultado = "Jogador Perdeu"
if player == "Tesoura" and pc == "Papel":
    resultado = "Jogador Ganhou"
if player == "Tesoura" and pc == "Tesoura":
    resultado = "Jogador Empatou"
    
# 03 - Resultado
print(resultado)
print("Jogador:", player, "/", "Pc:", pc)
