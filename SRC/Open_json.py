import json
def op(n): #OJOOO HAY QUE PONER EL NOMBRE DEL ARCHIVO JSON AL LLAMAR LA FUNCION PARA EL JSON QUE SE DESEA ABRIR
    with open((fr"D:\UNIVERSIDAD\PROYECTO MIPYMES\Proyecto_Mipymes_Brayan\JSON\{n}.json"), "r", encoding="utf-8") as f:
        datos = json.load(f)
    return(datos)