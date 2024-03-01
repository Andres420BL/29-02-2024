import os
os.system('cls')
codigoint = int(input('Codigo'))
nombreStr = input('Nombre')
existenciasint = 0
controlbln = True
while controlbln == True:
    os.system('cls')
    print('codigo',codigoint,'\nNombre',nombreStr,'\nexistenciasint: ',existenciasint)
    opcionStr = input('1.Compras.\n2.Ventas.\n.3.Reportes\n4.Salir--->')
    cantidadint= int(input('Cantidad'))
    if opcionStr == '1':
        existenciasint += cantidadint
    if opcionStr == '2':
        if cantidadint <= existenciasint:
            existenciasint -= cantidadint
        else:
            print('\nNo hay suficientes existencias')
        enter = input('<ENTER>')
    if opcionStr == '3':
        print('Cantidad actual de inventario:', existenciasint)
    if opcionStr == '4':
        controBln = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   