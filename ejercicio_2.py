#Roberto Carrasco Abarca 20.707.445-4
def areaC(r):
  resultado = r * r * 3.14
  return resultado


def VolC(h, r):
  vol = h * areaC(r)
  return vol


radio = float(input("Ingrese el radio del circulo: "))
Area = areaC(radio)

print("El Area es:", Area)
altura = float(input("Ingrese la altura del cilindro: "))
volumen = VolC(altura, radio)
print("El volumen del cilindro es:", volumen)
