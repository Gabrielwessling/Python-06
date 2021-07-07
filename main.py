import os

soma = 0
maior = 0
menor = 9999999
quantidadeNum = 0
porcentagemImpar = 0
quantidadeNumpar = 0
mediaPares = 0

def clear():
  os.system('cls' if os.name=='nt' else 'clear')

while True:
  clear()
  print("______________________________________________________________________")
  print("| Escreva um número para adicionar ou '30000' para parar de adicionar")
  num = int(input())
  if num == 30000:
    break
  if num >= maior:
    maior = num
  if num <= menor:
    menor = num
  if num%2 == 0:
    mediaPares = mediaPares + num
    quantidadeNumpar = quantidadeNumpar + 1
  if num%2 == 1:
    porcentagemImpar = porcentagemImpar + 1
  soma = soma + num
  quantidadeNum = quantidadeNum + 1

clear()
print("______________________________________________________________________")
print("| ")
print("|  Quantidade de números recebidos:", quantidadeNum)
print("|  Soma dos números:", soma)
print("|  Maior número recebido:", maior)
print("|  Menor número recebido:", menor)
print("|  Média entre números:", (soma / quantidadeNum))
print("|  Média entre números pares:", (mediaPares / quantidadeNumpar))
print("|  Porcentagem dos números ímpares recebidos:",(porcentagemImpar * 100 / quantidadeNum),"%")
print("|_____________________________________________________________________")