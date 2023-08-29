# ''''
# ##AULA DE OPERADORES
# 1. Crie um programa que peça um número e mostre o seu sucessor e antecessor

# '''

numero = input("Digite o Numero: ")

try:
    sucessor = int(numero) + 1
    antecessor = int(numero) - 1
except ValueError:
    print("Digite um número válido")
    raise ValueError
   
    
##impressão do Resultado
print(f"seu número digitado foi: {numero}, seu sucessor é {sucessor} e seu antecessor é {antecessor}")

