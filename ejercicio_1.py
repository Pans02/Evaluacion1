#Roberto Carrasco Abarca 20707445-4
puntos=input("Ingrese la puntuacion que a recibido el empleado: ")
puntuacion=float(puntos)
if (int(puntos[2])%2!=0):
    print("El nivel ingresado es incorrecto")
elif(puntuacion == 0.0):
    print("Su nivel es inaceptable por lo que recibe 0 de bonificacion")
elif(puntuacion==0.4):
    print("Su nivel es aceptable y recibe una bonificacion de ",puntuacion*2400," euros")
else:
    print("Su nivel es meritorio y recibe una bonificacion de ",puntuacion*2400," euros")