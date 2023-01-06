"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

quantidade_notas = 4
nota_1 = int(input("Nota B1: "))
nota_2 = int(input("Nota B2: "))
nota_3 = int(input("Nota B3: "))
nota_4 = int(input("Nota B4: "))

soma_notas = nota_1 + nota_2 + nota_3 + nota_4
media_notas = soma_notas / quantidade_notas

print(f'A media das notas: {media_notas}')
