#!/bin/sh
import fileinput

tableau = [['E','N','C','R','Y'],['P','T','A','B','D'],['F','G','H','I','K'],['L','M','O','Q','S'],['U','V','W','X','Z']]
mensajecif=[]
filas = []
columnas = []
nuevospares = []
###ELIMINAR ESPACIOS EN MENSAJE E INSERTARLO EN UNA LISTA 
mensaje = 'TRAVEL NORTH AT ONCE'

#for indice, numero in enumerate(mensaje2):

##RECORRER EL TABLEAU E IMPRIMIR NUMERO DE FILA Y COLUMNA 

def cifrar(mensaje):

	mensaje2= list(mensaje.replace(" ",""))
	print(mensaje2)
	indice = 0 
	fil=0
	col=0
	for indice, numero in enumerate(mensaje2):
			for fila in tableau:
				for elemento in fila:
					#print('elemento[{}][{}]: {} '.format(fil,col,elemento))
					if mensaje2[indice] == elemento:
						#print('{} {}\n'.format(fil,col))
						clave = '{}{}'.format(fil,col)
						mensajecif.append(clave)
						filas.append(fil)
						columnas.append(col)
						nuevospares = filas + columnas
					col+=1
				col = 0 
				fil+=1
			fil = 0

	print(mensajecif)
	print(filas)
	print(columnas)
	print(nuevospares,'\n\n\n')
	i = 0
	j = 1
	cifrado = ''
	##Formar el mensaje en cifrado 
	for indice, elemento in enumerate(nuevospares):
		try:
			print(indice)
			print('{} {}'.format(nuevospares[i],nuevospares[j]))
			print('letra cifrada: {} '.format(tableau[nuevospares[i]][nuevospares[j]]))
			cifrado = cifrado + tableau[nuevospares[i]][nuevospares[j]]
			print('\n')
			i+= 2 
			j += 2
		except: 
			print('error')
			break

	print(cifrado)

def descifrar(cifrado):
	fil = 0 
	col = 0 

	for indice, numero in enumerate(cifrado):
		for fila in tableau:
			for elemento in fila: 
				if cifrado[indice] == elemento:
					print('{}{}'.format(fil,col))
				col += 1
			col = 0
			fil += 1
		fil = 0 


#cifrar('TRAVEL NORTH AT ONCE')
descifrar('LNLLFGPPNPGRSK')



