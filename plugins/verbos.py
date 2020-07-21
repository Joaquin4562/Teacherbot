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
            traduccion = sheet.cell_value(i,0)
            pasado = sheet.cell_value(i,1)
            participio = sheet.cell_value(i,2)
            return 'set_slot {0} "traducción {1}, pasado {2}, participio {3}"'.format(var, traduccion, pasado, participio)

    return 'set_slot datos "No se encontro la palabra"'


