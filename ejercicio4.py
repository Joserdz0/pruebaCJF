def encontrar_rutas(elementoJuridicoInicial, elementoJuridicoFinal, relaciones):
    rutas = []  # Lista para almacenar todas las rutas encontradas
    ruta_actual = [elementoJuridicoInicial]  # Ruta actual que se está explorando
    
    # Función auxiliar recursiva para encontrar las rutas
    def encontrar_rutas_recursivo(elemento_actual):
        if elemento_actual == elementoJuridicoFinal:  # Se ha llegado al elemento final, se agrega la ruta a la lista de rutas
            rutas.append(list(ruta_actual))  # Usamos list() para crear una copia independiente de la ruta_actual
        else:
            for relacion in relaciones:
                if relacion[0] == elemento_actual and relacion[1] not in ruta_actual:
                    ruta_actual.append(relacion[1])  # Agregar el siguiente elemento a la ruta_actual
                    encontrar_rutas_recursivo(relacion[1])  # Llamada recursiva para continuar explorando
                    ruta_actual.pop()  # Retroceder: eliminar el último elemento agregado a la ruta_actual
    
    encontrar_rutas_recursivo(elementoJuridicoInicial)  # Llamada inicial a la función auxiliar
    
    return rutas

# Ejemplo de uso
relaciones = [
    ('Principio de Contradiccion', 'Sentencia 338/2018'),
    ('Juez de Amparo', 'Tribunal Colegiado'),
    ('Auto de Vinculacion a Proceso', 'Juez de Control'),
    ('Organo Jurisdiccional', 'Juez de Control'),
    ('Juzgado de Control', 'Sentencia 338/2018'),
    ('Juzgado de Distrito', 'Sentencia 338/2018'),
    ('Norma Convencional que contempla justa indemnizacion', 'Sentencia 423/2019'),
    ('Autoridad Jurisdiccional', 'Suprema Corte de Justicia de la Nacion'),
    ('Organo Jurisdiccional', 'Juez de Amparo'),
    ('Norma Convencional que contempla justa indemnizacion', 'Articulo 63.1 Convencion Americana sobre Derechos Humanos'),
    ('Juez de Amparo', 'Juzgado de Distrito'),
    ('Tribunal Colegiado', 'Sentencia 338/2018'),
    ('Norma Convencional que contempla justa indemnizacion', 'Norma Convencional'),
    ('Prision Preventiva Oficiosa', 'Organo Jurisdiccional'),
    ('Autoridad Jurisdiccional', 'Organo Jurisdiccional')
]

rutas = encontrar_rutas('Juez de Amparo', 'Sentencia 338/2018', relaciones)
for ruta in rutas:
    print(ruta)