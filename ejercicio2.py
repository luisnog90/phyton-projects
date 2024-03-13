def letras_unicas(palabra):
    # Crear un conjunto vacío para almacenar letras únicas
    letras_unicas = set()
    # Iterar sobre cada letra de la palabra
    for letra in palabra:
        # Agregar la letra al conjunto 
        letras_unicas.add(letra)
    # Convertir el conjunto en una lista para poder ordenarla y luego ordenarla alfabéticamente        
    letras_unicas = list(letras_unicas)
    letras_unicas.sort()
    return letras_unicas

# recepcion de la palabra
palabra = input("ingrese la palabra: ")
letras = letras_unicas(palabra)
#impresion
print(f"las letras sin repetir y organizadas de su palabra son: {letras}")
