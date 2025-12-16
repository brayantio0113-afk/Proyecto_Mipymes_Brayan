import Open_json
from Open_json import op

#EXTRAER UNA LISTA CON LOS PRECIOS DEL DOLLAR EN EL TOQUE
def usd():
    u=[]
    for i in (op("ElToque")["ElToque"]):
        u.append(i["USD"])
    return (u)

#EXTRAER UNA LISTA CON LAS FECHAS ANALIZADAS DE EL TOQUE
def fechas_eltoque():
    f=[]
    for i in (op("ElToque")["ElToque"]):
        f.append(i["Fecha"])
    return(f)

#EXTRAER UNA LISTA CON LOS PRECIOS DEL EURO EN EL TOQUE
def euro():
    e=[]
    for i in (op("ElToque")["ElToque"]):
        e.append(i["EURO"])
    return(e)

#EXTRAER UNA LISTA CON LOS PRECIOS DEL MLC EN EL TOQUE
def mlc():
    m=[]
    for i in (op("ElToque")["ElToque"]):
        m.append(i["MLC"])
    return(m)

# DICCIONARIO CON LA CANTIDAD DE CADA PRODUCTO
def cantidad_productos():

    mp=op("Mipymes")["mipymes"]
    c1=-1
    prod=[]
    cant_prod={}
    for j in range(30):
        c1+=1
        for i in(mp[c1]["productos"]):
            prod.append(i["tipo"])
    for k in prod:
        if k in cant_prod:
            cant_prod[k] += 1
        else:
            cant_prod[k] = 1
    return(cant_prod)

#DICCIONARIO BOOLEANO QUE DICE CAUNTAS MIPYMES ALCANZA PARA COMPRAR UNA UNIDAD DE CADA PRODUCTO CON EL SALARIO PROMEDIO
def alc_salario():
