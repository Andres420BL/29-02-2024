#Elaborar un programa en Python el cual tiene los siguientes productos: 1. Computador de escritorio 2. Computador de escritorio 3. Tabletas 4. Videobeam 5. Televisores y determinar cuantos de cada uno se han comprado, tener en cuenta que el precio de los artículos debe estar establecidos de manera constante, el sistema debe recibir todos los productos de manera infinita y al momento de seleccionar la opción de “FACTURAR” debe mostrar el total de la suma de los artículos, cuantos de cada uno se agregaron, el total a pagar. 

cons_portatil = 2000000
cons_pcmesa=2800000
cons_tabletas = 500000
videobeam = 800000
televisor = 2000000

cportatil = 0
cpcmesa= 0
ctabletas = 0
cvideobeam = 0
ctelevisor = 0

total = 0
controlBln = True
while (controlBln == True):
    print('\t.Tienda de tecnologia:\n.0.Facturacion.\n.1.Portatil 2000000 $.\n.2.Pc de escritorio 2800000 $.\n.3.Tableta 500000 $.\n. 4 videobeam 800000 $.\n.5 Televisor 2000000 $')

    opcion = int(input('--->'))
    
    if opcion == 0:
       controlBln = False
        
    if opcion == 1:
        total += cons_portatil
        cportatil += 1
        
    if opcion == 2:
        total += cons_pcmesa
        cpcmesa += 1

    if opcion == 3:
        total += cons_tabletas
        ctabletas += 1
        
    if opcion == 4:
        total += videobeam
        cvideobeam += 1   
        
    if opcion == 5:
        total += televisor
        ctelevisor += 1 
    if opcion != 0:
        input('Compra realizada con exito')
    
if total !=0:
    print('<<Facturación>>')
    print('\nComputador portatil: ', cportatil)
    print('\nComputador de mesa:',cpcmesa)
    print('\nTabletas: ', ctabletas)
    print('\nVideobeams:',cvideobeam)
    print('\nTelevisores:',ctelevisor)
    print('\nTotal a pagar:', total)
        
    
  
        
        
        
    
