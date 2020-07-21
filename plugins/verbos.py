import xlrd

def buscar(*verb):
    filePath = 'lista_verbos.xlsx'
    openFile = xlrd.open_workbook(filePath)
    sheet = openFile.sheet_by_name('hoja1')
    for i in range(sheet.nrows):
        valor = sheet.cell_value(i,3)
        if(valor == verb):
            traduccion = sheet.cell_value(i,0)
            pasado = sheet.cell_value(i,1)
            participio = sheet.cell_value(i,2)
            return 'set_slot datos " traducción {0}, pasado {1}, participio {2}"'.format(traduccion, pasado, participio)
