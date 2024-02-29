#Elaborar un programa en Python que permita capturar una cantidad N de númerosy permita determinar cuántos de estos números se encuentran en el rango de 10 – 20. 

cantidad = int(input('Ingrese la cantidad de números a digitar --> '))
#inicializa contador
contador = 0

#ESTRUCTURA WHILE
while (contador < cantidad) :
    numero = int(input('Digite un numero'))
    if numero >10 and  numero <20:
        print('ESTAS DENTRO DEL RANGO')
    else:
        print('ESTAS fuera del rango')
    contador = contador + 1
    


    
    