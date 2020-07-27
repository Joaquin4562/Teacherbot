import random
from os.path import join, dirname, abspath
def generarPregunta():
    long = obtenerLongitud()
    if long > 0:
        pregunta = random.randint(1,3)
        verbo = random.randint(1,long)
        contador = 1
        file = open (join(dirname(dirname(abspath(__file__))), 'plugins', 'verbosEstudiados.txt'), 'r')
        verboElegido = ""
        preguntaElegida = ""
        while (True):
            verboElegido = file.readline().strip()
            if contador==verbo:
                break
            contador+=1    
        file.close()
        preguntasAElegir = {'1':"Dime la traducción al Inglés de ", '2':"Dime el pasado de ", '3':"Dime el participio de "}
        preguntaElegida = preguntasAElegir[str(pregunta)]
        preguntaCompleta = preguntaElegida + verboElegido
        return 'set_slot preguntas ["{0}","{1}","{2}"]'.format(preguntaElegida, verboElegido, preguntaCompleta)
    else:
        return 'say "Aun no has estudiado nada"'   
#Metodo de apoyo
def obtenerLongitud():
    file = open (join(dirname(dirname(abspath(__file__))), 'plugins', 'verbosEstudiados.txt'), 'r')
    contador = 0
    while(True):
        linea = file.readline().strip()
        if not linea:
            break
        else:
            contador+=1
    return contador