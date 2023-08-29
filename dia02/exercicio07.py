'''Crie um programa que va de 0 à 30, mas pare qunado encontrar o 20'''

i = 0
while i <= 30:
    print(i)
    i+=1
    if i == 20:
     print(f"Chegou no {i}, Fim do Programa")
     break