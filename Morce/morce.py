# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 02:06:42 2020

@author: PCMiguel
"""

def get_key(diccionario, val):
    for key, value in diccionario.items():
        if val == value:
            return key
    return ''

diccionario = {}

diccionario['a'] = '.-'
diccionario['b'] = '-...'
diccionario['c'] = '-.-.'
diccionario['d'] = '-..'
diccionario['e'] = '.'
diccionario['f'] = '..-.'
diccionario['g'] = '--.'
diccionario['h'] = '....'
diccionario['i'] = '..'
diccionario['j'] = '.---'
diccionario['k'] = '-.-'
diccionario['l'] = '.-..'
diccionario['m'] = '--'
diccionario['n'] = '-.'
diccionario['o'] = '---'
diccionario['p'] = '.--.'
diccionario['q'] = '--.-'
diccionario['r'] = '.-.'
diccionario['s'] = '...'
diccionario['t'] = '-'
diccionario['u'] = '..-'
diccionario['v'] = '...-'
diccionario['w'] = '.--'
diccionario['x'] = '-..-'
diccionario['y'] = '-.--'
diccionario['z'] = '--..'
diccionario[' '] = '/'

#PASAR DE ABECEDARIO A MORCE

def abc_morce(cadenaNormal):
    cadenaMorce = ''
    
    for caracter in cadenaNormal:
        cadenaMorce = cadenaMorce + diccionario[caracter] + ' '
        
    print(cadenaMorce)

#DE CODIGO MORCE A ABECEDARIO
def morce_abc(cadenaMorce):

    morce_tokens = cadenaMorce.split()
    
    morceCadena = ''
    for token in morce_tokens:
        morceCadena = morceCadena + get_key(diccionario, token)
        
    print(morceCadena)

# Imprimimos el menú en pantalla
print("1. PASAR DE ABECEDARIO A CODIGO MORCE")
print("2. PASAR DE CODIGO MORCE A ABECEDARIO")
print("0. SALIR")
# Leemos lo que ingresa el usuario
opc = input("DIGITE SU OPCION: ")


#Se  implementa el menu 
def menu(opc):
    while True:
        if opc=="1":
            cadenaNormal = str(input('INGRESE LA CADENA: '))
            abc_morce(cadenaNormal)
            break
        elif opc=="2":
            cadenaMorce = str(input('INGRESE LA CADENA: '))
            morce_abc(cadenaMorce)
            break
        elif opc=="0":
            print("UD HA SALIDO")
            break
        else:
            print("OPCION NO VALIDA");
            break

menu(opc)


    