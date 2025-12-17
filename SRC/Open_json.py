import json
def op(n):
    with open((fr"D:\UNIVERSIDAD\PROYECTO MIPYMES\JSON\{n}.json"), "r", encoding="utf-8") as f:
        datos = json.load(f)
    return(datos)