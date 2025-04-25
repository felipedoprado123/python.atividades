#  Como calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção,
#  considerando que cada blusa requer uma quantidade de 120 metros de fio e que cada novelo contém 125 de metros de fio?

blusas = float(input("Insira a quantidade blusas que deseja:"))

quantidade = (120 * blusas) / 125

print(f"A Quantidade de novelos delã é {quantidade:.0f}") # Arredodar pois nao tem como comprar 0,5 de novelo de lã
