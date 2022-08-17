# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# INSERTE SU IMPORTACIÓN
# from <LIBRERÍA> import <FUNCIÓN>
from random import shuffle
def generar_baraja(tipos_cartas, n_palos):
    # ACÁ INICIA LA FUNCIÓN
    
    baraja = []
    i = 0
    while i < n_palos:
        for carta in tipos_cartas:
            baraja.append(carta)
        i += 1

        
    shuffle(baraja)
    baraja= tuple(baraja)
    
    # ACÁ TERMINA LA FUNCIÓN
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return baraja
    