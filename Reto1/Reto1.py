"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""
from student_utilities import input, print


def solucion(b,n):
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    control = 0
    
    
    intentos = 0
        
    while( control == 0):
        
        num = int(input("Ingrese un número:"))
                    
        if (num < 0) or (num > b):
            print('¡Te saliste del intervalo!')
            
        
        elif (num > n):
            print('¡Ups! Te pasaste')
            intentos += 1
        
        
        elif (num < n):
            print('¡Ups! Estás por debajo')
            intentos += 1
        
        
        else:
            intentos += 1
            print(f'¡LO LOGRASTE! Usaste {intentos} intentos' )
            control = 1
    
    
    
    #ACÁ TERMINA LA FUNCIÓN SOLUCIÓN
"""
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN calcular_promedio_y_cuadro_honor(grupo) .
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA
"""