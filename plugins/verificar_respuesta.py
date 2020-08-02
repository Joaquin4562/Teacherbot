import xlrd
from os.path import join, dirname, abspath

def verificarRespuesta(verb, pregunta, respuesta):
    filePath = join(dirname(dirname(abspath(__file__))), 'plugins', 'lista_verbos.xlsx')
    openFile = xlrd.open_workbook(filePath)
    sheet = openFile.sheet_by_name('Hoja 1')
    for i in range(sheet.nrows):
        valor = sheet.cell_value(i,3)
        if(valor == verb):
            respuestaCorrecta = sheet.cell_value(i, int(pregunta))
            if respuestaCorrecta == respuesta:
                return "execute self.slots['cont_correcto']+=1"
            else:
                return "execute self.slots['cont_incorrecto']+=1"
        
    return 'say "No se entendio tu respuesta"'