import xlrd
from os.path import join, dirname, abspath

def buscar(verb):
    filePath = join(dirname(dirname(abspath(__file__))), 'plugins', 'lista_verbos.xlsx')
    var = "datos"
    openFile = xlrd.open_workbook(filePath)
    sheet = openFile.sheet_by_name('Hoja 1')
    for i in range(sheet.nrows):
        valor = sheet.cell_value(i,3)
        if(valor == verb):
            agregarVerbo(verb)
            traduccion = sheet.cell_value(i,0)
            pasado = sheet.cell_value(i,1)
            participio = sheet.cell_value(i,2)
            return 'set_slot {0} "traducción {1}, pasado {2}, participio {3}"'.format(var, traduccion, pasado, participio)

    return 'set_slot datos "Lo siento, aun no entiendo esa palabra"'

def agregarVerbo(verbo):
    if buscarSiExiteVerbo(verbo)==False:
        file = open (join(dirname(dirname(abspath(__file__))), 'plugins', 'verbosEstudiados.txt'), 'r')
        linea = file.readline().strip()
        file.close()
        file = open (join(dirname(dirname(abspath(__file__))), 'plugins', 'verbosEstudiados.txt'), 'a')
        if linea!="": 
            file.write('\n'+verbo)
            file.close()
        else:
            file.write(verbo)
            file.close()

def buscarSiExiteVerbo(verbo):
    file = open (join(dirname(dirname(abspath(__file__))), 'plugins', 'verbosEstudiados.txt'), 'r')
    while(True):
        linea = file.readline().strip()
        if (verbo==linea):
            return True
        if not linea:
            break      
    return False 
    file.Close()