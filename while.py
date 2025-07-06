numero_sorteado = 15

numero_escolhido = int(input("Digite um número entre 1 e 20: "))

# if numero_sorteado == numero_escolhido:
#     print("Parabéns, você acertou!")
# else:
#     print("Você errou, tente novamente!")


while numero_escolhido != numero_sorteado:
 print("Você errou, tente novamente!")
 
 numero_escolhido = int(input("Digite um número entre 1 e 20: "))
 
print("Parabéns, você acertou!")


#exemplo 2:Estrutura com Contador 

contador= 0

while contador < 5:
    print(contador)
    contador =contador +1