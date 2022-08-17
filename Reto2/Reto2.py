# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO ELIMINAR LA IMPORTACIÓN
from string import ascii_uppercase as alfabeto

# NO MODIFICAR LOS NOMBRES, PARÁMETROS O RETORNOS DE LAS FUNCIONES
def encriptador(mensaje):
    # ACÁ INICIA LA FUNCIÓN ENCRIPTADOR
    # (En este espacio debes poner el código necesario para encriptar)
    
    mensaje1=list(set(mensaje))
    palabra=list(alfabeto)
    print (alfabeto)

    M= []
    clave={}
    i=0
    while i<len(mensaje1):
        clave[mensaje1[i]]=palabra[i]
        i=i+1

    for i in range(len(mensaje)):
        P = mensaje[i]
        Q = clave[P]
        M.append(Q)
    encriptado=''.join(M)
    print(f'encriptado: {encriptado}')
    
    desencriptador(encriptado,clave)
    return encriptado,clave 
    
    # ACÁ TERMINA LA FUNCIÓN ENCRIPTADOR
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return encriptado, clave

    
def desencriptador(encriptado, clave):
    # ACÁ INICIA LA FUNCIÓN DESENCRIPTADOR 
    # (En este espacio debes poner el código necesario para desencriptar)
    T =[]
    nuevaclave={}
    encriptado=list(encriptado)
    clave=dict(clave)
    nuevaclave={v:k for k, v in clave.items()}
    for i in range(len(encriptado)):
        R=encriptado[i]
        S=nuevaclave[R]
        T.append(S)
    desencriptado=''.join(T)

    print(desencriptado)
    
    
    # ACÁ TERMINA LA FUNCIÓN DESENCRIPTADOR
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return desencriptado

