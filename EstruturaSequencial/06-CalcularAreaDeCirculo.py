"""
Faça um Programa que peça o raio de um círculo,
calcule e mostre sua área.
"""

from math import pi

raio = float(input("Informe o raio: "))
area = pi * raio ** 2

print(f'A area do circulo é {area:,.2f}')
