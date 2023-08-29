# '''Crie um programa que receba uma idade e retorne se pode obter carteira de MOTORISTA (CNH)'''

idade = input("Digite a sua Idade: ")

try:
    idade = int(idade)
    if idade >= 18:
        print("Você está apto para ter CNH")
    elif idade >= 16:
        print("Você pode tirar se quiser.")
    else:
        print("Você não está apto para receber")
    
except ValueError:
    print("Digite apenas números")
    


