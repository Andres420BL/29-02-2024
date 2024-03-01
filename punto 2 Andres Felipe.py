controlbln = True
telvisorFlt = 1000000
computdor_portatilflt= 2000000
computador_escritorioflt = 3000000
videobeamflt = 2000000
tabletasflt = 1000000
#valores finales
ctv = 0
totales_tv = 0
ccomputador_portatil = 0
total_portatil = 0
ccomputador_escritorio = 0
total_escritorio = 0
cvideobeam = 0
total_videobeam = 0
ctabltas = 0
total_tabletas = 0
import os
os.system('cls')

while controlbln == True:
    opcionStr = input('1.computador de escritorio\n2.computador portatil \n3.Tabletas\n4.Videobeam\n5.Televisor\n6.Factuar\n7.Salir->')
    if opcionStr == '1':
        ccomputador_escritorio += 1
        total_escritorio += computador_escritorioflt   
    if opcionStr == '2':
        ccomputador_portatil += 1
        total_portatil += computdor_portatilflt
    if opcionStr == '3':
        ctabltas += 1
        total_tabletas += tabletasflt
    if opcionStr == '4':
        cvideobeam += 1
        total_videobeam += videobeamflt
    if opcionStr == '5':
        ctv += 1
        totales_tv += telvisorFlt
    if opcionStr == '6':
        print('Cantidad de computadores de escrotorio...............................',ccomputador_escritorio ,'$',total_escritorio)
        print('Cantidade de computadores portatailes.................................',ccomputador_portatil,'$',total_portatil)
        print('Cantidad de tabletas...................................................',ctabltas,'$',total_tabletas)
        print('Cantidad de videobeam.................................................',cvideobeam,'$',total_videobeam)
        print('Cantidad de tv.........................................................',ctv,'$',totales_tv)
        print('Total de ventas $.........................................................................',(totales_tv + total_escritorio + total_portatil + total_tabletas + total_videobeam))
        enter = input('\n<ENTER>')
        if opcionStr == '7':
            controlbln = False
        
    