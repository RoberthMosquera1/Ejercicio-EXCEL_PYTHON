from datetime import datetime
from openpyxl import load_workbook

def borrar(ruta,identificador):
    Archivo_Excel = load_workbook(ruta)
    Hoja_datos = Archivo_Excel['Datos_tarea']
    Hoja_datos=Hoja_datos['A2':'F'+str(Hoja_datos.max_row)]
    hoja=Archivo_Excel.active

    titulo=2
    descripcion=3
    estado=4
    fecha_inicio=5
    fecha_Finalizado=6
    encontro=False
    for i in Hoja_datos:
        if i[0].value==identificador:
            fila=i[0].row
            encontro=True

            hoja.cell(row=fila, column=1).value=""
            hoja.cell(row=fila, column=titulo).value=""
            hoja.cell(row=fila, column=descripcion).value=""
            hoja.cell(row=fila, column=estado).value=""
            hoja.cell(row=fila, column=fecha_inicio).value=""
            hoja.cell(row=fila, column=fecha_Finalizado).value=""
    Archivo_Excel.save(ruta)
    if encontro==False:
        print('Error: No existe una tarea con ese id')
        print()
    return