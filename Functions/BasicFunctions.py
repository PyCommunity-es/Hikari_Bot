

def config():
    # Inserción del token
    return input("Escribe el token: ")

def definiciones(palabra):
    """ Definiciones de palabras """
    
    from Resources.DataBase import definiciones
    
    if palabra in definiciones.keys(): # Buscamos en el diccionario  
        return definiciones[palabra]
    else:
        import wikipedia # Buscamos la definicion en Wikipedia
        wikipedia.set_lang("es")
        
        try: 
            resumen = wikipedia.summary(palabra, sentences = 1)
            url = (wikipedia.page(palabra).url)
            return (resumen + "\n\nMas info: " + url)
        except: 
            return "No se ha encontrado esta definicion..."

def saludo():
    from Resources.DataBase import saludo
    from random import choice
    return choice(saludo)

def help():
    from Resources.DataBase import msj_help
    return msj_help

def rules():
    from Resources.DataBase import rules
    return rules
