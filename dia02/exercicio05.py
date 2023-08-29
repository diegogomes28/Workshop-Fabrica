#''' Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h e mostre que ele foi multado a 7 reais por cada KM '''***'''


velocidade = input("Digite a Velocidade percorrida: ") #Pede a entrada de velocidade

try:
    velocidadeinteira = float(velocidade) #conversão do tipo p float
    if velocidadeinteira > 80.00:
        print(f"Você foi Multado") 
        print(f"Multa no valor de {(velocidadeinteira - 80)*7}")
    else:
        print("Tudo certo.")

except ValueError: #verifica se codigo acima foi executado.
    print("Digite apenas números")