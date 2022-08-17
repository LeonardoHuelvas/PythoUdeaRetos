alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encriptar_caracter(caracter_encriptado, b):
    lista_alfabeto=list(alfabeto)

    posicion_encriptada=0
    for i in range(len(lista_alfabeto)):
        if caracter_encriptado==lista_alfabeto[i]:
            posicion_encriptada=(i+b)%27
            caracter_encriptado=lista_alfabeto[posicion_encriptada]
            break
    return caracter_encriptado
    
def encriptar(mensaje, b):
    list_mensaje=list(mensaje)
    mensaje_encriptado=""
    for i in range(len(list_mensaje)):
        mensaje_encriptado=mensaje_encriptado+str(encriptar_caracter(list_mensaje[i],b))

    return mensaje_encriptado
    
def desencriptar_caracter(caracter_encriptado, b):
    lista_alfabeto=list(alfabeto) 
    posicion_desencriptada=0
    caracter_desencriptado=""
    encontrado=False 
    for i in range(len(lista_alfabeto)):
        if caracter_encriptado==lista_alfabeto[i]:
            posicion_desencriptada=(i-b)%27
            caracter_desencriptado=lista_alfabeto[posicion_desencriptada]
            encontrado=True
            break
    if encontrado==False:
        caracter_desencriptado=caracter_encriptado
    
    return caracter_desencriptado
    
def desencriptar(mensaje_encriptado, b):
    list_mensaje=list(mensaje_encriptado)
    print(list_mensaje)
    list_desencriptado=[]
    for i in range(len(list_mensaje)):
            list_desencriptado.append(desencriptar_caracter(list_mensaje[i],b))
            
    mensaje_desencriptado="".join(list_desencriptado)
    
    return mensaje_desencriptado