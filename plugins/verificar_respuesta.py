import xlrd
from os.path import join, dirname, abspath

def verificarRespuesta(verb, pregunta, respuesta):
    filePath = join(dirname(dirname(abspath(__file__))), 'plugins', 'lista_verbos.xlsx')
    openFile = xlrd.open_workbook(filePath)
    sheet = openFile.sheet_by_name('Hoja 1')
    for i in range(sheet.nrows):
        valor = sheet.cell_value(i,3)
        if(valor == verb):
            traduccion = sheet.cell_value(i,0)
            pasado = sheet.cell_value(i,1)
            participio = sheet.cell_value(i,2)
            if pregunta == "Dime la traducción al Inglés de ":
                if traduccion == respuesta:
                    return 'say "Respuesta Correcta"'
                else :
                    return 'say "Respuesta Incorrecta"'

            if pregunta == "Dime el pasado de ":
                if pasado == respuesta:
                    return 'say "Respuesta Correcta"'
                else :
                    return 'say "Respuesta Incorrecta"'

            if pregunta == "Dime el participio de ":
                if participio == respuesta:
                    return 'say "Respuesta Correcta"'
                else :
                    return 'say "Respuesta Incorrecta"'
    return 'say "No se entendio tu respuesta, puto"'