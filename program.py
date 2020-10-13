#!/bin/sh
import fileinput

tableau = [['E','N','C','R','Y'],['P','T','A','B','D'],['F','G','H','I','K'],['L','M','O','Q','S'],['U','V','W','X','Z']]
mensajecif=[]
filas = []
columnas = []
nuevospares = []
nuevalista = []



def cifrar(mensaje):
	###ELIMINAR ESPACIOS EN MENSAJE E INSERTARLO EN UNA LISTA 
	mensaje2= list(mensaje.replace(" ",""))
	indice = 0 
	fil=0
	col=0
	for indice, numero in enumerate(mensaje2):
			for fila in tableau:
				for elemento in fila:
					if mensaje2[indice] == elemento:
						filas.append(fil)
						columnas.append(col)
						nuevospares = filas + columnas
					col+=1
				col = 0 
				fil+=1
			fil = 0

	i = 0
	j = 1
	cifrado = ''
	##FORMAR EL MENSAJE CIFRADO
	for indice, elemento in enumerate(nuevospares):
		try:
			cifrado = cifrado + tableau[nuevospares[i]][nuevospares[j]]
			i+= 2 
			j += 2
		except: 
			break

	print(cifrado)


def descifrar(cifrado):
	fil = 0 
	col = 0 

	for indice, numero in enumerate(cifrado):
		for fila in tableau:
			for elemento in fila: 
				if cifrado[indice] == elemento:
					filas.append(fil)
					columnas.append(col)
					nuevospares.append(fil)
					nuevospares.append(col)
				col += 1
			col = 0
			fil += 1
		fil = 0 

	dividir = int(len(nuevospares) / 2)
	lista1 = nuevospares[:dividir]
	lista2 = nuevospares[dividir:]

	for i,e  in enumerate(lista1):
		nuevalista.append(e)
		nuevalista.append(lista2[i])

	descifrado = ''
	for i,e in enumerate(nuevalista):
		if i % 2 == 0: 
			descifrado = descifrado + tableau[e][nuevalista[i+1]]
			
	print(descifrado)



	#print('filas : \n',filas)
	#print('columnas: \n',columnas)
	#print(nuevospares)

#cifrar('TRAVEL NORTH AT ONCE')
#descifrar('LNLLFGPPNPGRSK')

archivo = fileinput.input()
leerlinea = archivo.readline()
seleccion = leerlinea.rstrip('\n')
if seleccion == 'ENCRYPT':
	leerlinea = archivo.readline()
	mensaje = leerlinea.rstrip('\n')
	cifrar(mensaje)
elif seleccion == 'DECRYPT':
	leerlinea = archivo.readline()
	cifrado = leerlinea.rstrip('\n')
	descifrar(cifrado)
else:
	print('seleccion incorrecta')






