from Open_json import op
#EXTRAER UNA LISTA CON LOS PRECIOS DEL USD EN EL TOQUE
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

# DICCIONARIO CON LA FRECUENCIA DE CADA PRODUCTO
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

#DICCIONARIO BOOLEANO QUE DICE CAUNTAS MIPYMES ALCANZA PARA COMPRAR UNA UNIDAD DE CADA PRODUCTO CON EL SALARIO PROMEDIO (5839)
def alc_salario_dic():
    mp=op("Mipymes")["mipymes"]
    total=0
    totales=[]
    salario={"si":0,
            "no":0}
    c=-1
    for j in range(30):
        total=0
        c+=1
        for i in (mp[c]["productos"]):
            total+=(int(i["price"]))
        totales.append(total)

    for i in totales:
        if i<=5839:
            salario["si"]+=1
        else: salario["no"]+=1
    return(salario)

#LISTA BOOLENA (0=NO/1=SI) QUE DICE LAS MIPYMES EN LAS QUE ALCANZA PARA COMPRAR UNA UNIDAD DE CADA PRODUCTO CON EL SALARIO PROMEDIO (5839)
def alc_salario_list():
    mp=op("Mipymes")["mipymes"]
    total=0
    totales=[]
    salario=[]
    c=-1
    for j in range(30):
        total=0
        c+=1
        for i in (mp[c]["productos"]):
            total+=(int(i["price"]))
        totales.append(total)
    for i in totales:
        if i>5839:
            salario.append(0)
        else: salario.append(1)
    return salario

#DICCIONARIO CON LA CANTIDAD DE METODOS DE PAGO EN LAS MIPYMES
def met_pago():
    moneda={"Euro":0,
            "USD":0,
            "MLC":0,
            "CUP":0}
    c=0
    mp=op("Mipymes")["mipymes"]
    for i in range(30):
        if mp[c]["moneda y metodos de pago"]["Euro"]!="None":
            moneda["Euro"]+=1
        if mp[c]["moneda y metodos de pago"]["USD"]!="None":
            moneda["USD"]+=1
        if mp[c]["moneda y metodos de pago"]["MLC"]!="None":
            moneda["MLC"]+=1
        if mp[c]["moneda y metodos de pago"]["CUP"]!="None":
            moneda["CUP"]+=1
        c+=1
    return (moneda)

#PROMEDIO (INT) DE LAS MONEDAS DE ELTOQUE EN EL MES DE OCTUBRE (LA FUNCION SIRVE PARA LAS 3 MONEDAS)
def prom_oct_et(moneda):
    promedio=0
    for i in moneda[0:31]:
        promedio+=i
    return(promedio//31)

#PROMEDIO (INT) DE LAS MONEDAS DE ELTOQUE EN EL MES DE NOVIEMBRE (LA FUNCION SIRVE PARA LAS 3 MONEDAS)
def prom_nov_et(moneda):
    promedio=0
    for i in moneda[31:61]:
        promedio+=i
    return(promedio//30)

#PROMEDIO (INT) DE LOS PRECIOS DEL ACEITE EN GRUPOS Y REVOLICO EN EL MES DE OCTUBRE
def prom_ac_grup_oct():
    c=-1
    promedio=0
    gr=op("Grupos")["Grupos_Revolico"][0]["Aceite"][0]["Octubre"]
    for i in range(30):
        c+=1
        promedio+=(gr[c]["CUP"])
    return(promedio//30)

#PROMEDIO (INT) DE LOS PRECIOS DEL ACEITE EN GRUPOS Y REVOLICO EN EL MES DE NOVIEMBRE
def prom_ac_grup_nov():
    c=-1
    promedio=0
    gr=op("Grupos")["Grupos_Revolico"][0]["Aceite"][1]["Noviembre"]
    for i in range(30):
        c+=1
        promedio+=(gr[c]["CUP"])
    return(promedio//30)

#LISTA CON LOS ID DE LOS DIAS DEL ANALISIS DEL TOQUE
def id_eltoque():
    id=[]
    for i in (op("ElToque")["ElToque"]):
        id.append(i["ID"])
    return(id)

#LISTA CON LOS NOMBRES DE LAS MIPYMES EN EL MISMO OREDEN DEL JSON
def nombres_mp():
    mp=op("Mipymes")
    nombres=[]
    c=0
    for i in range(30):
            nombres.append (mp["mipymes"][c]["nombre"])
            c+=1
    return nombres 

#DICCIONARIO CON LOS METODOS DE PAGO ACEPTADOS EN CADA MIPYME
def met_pago_dicc():
    mp=op("Mipymes")
    resultado = {}

    for i in mp["mipymes"]:
        nombre = i["nombre"]
        pagos = i["moneda y metodos de pago"]

        monedas = []
        for moneda, metodo in pagos.items():
            if metodo != "None":
                monedas.append(moneda)

        resultado[nombre] = monedas

    return resultado

#DICCIONARIO QUE MUESTRA LOS NOMBRES DE LAS MIPTMES Y LA SUMA DE SUS PRODUCTOS
def alc_salario_nombres_dicc():
    mp=op("Mipymes")["mipymes"]
    nombres=nombres_mp()
    nombres
    total=0
    totales=[]
    salario={}
    c=-1
    for j in range(30):
        total=0
        c+=1
        for i in (mp[c]["productos"]):
            total+=(int(i["price"]))
        totales.append(total)
    salario=dict(zip(nombres, totales))
    return salario

#PROMERIO DEL PRECIO DEL ARROZ EN OCTUBRE
def prom_arr_grup_nov():
    c=-1
    promedio=0
    gr=op("Grupos")["Grupos_Revolico"][0]["Arroz"][0]["Noviembre"]
    for i in range(30):
        c+=1
        promedio+=(gr[c]["CUP"])
    return(promedio//30)

#PROMERIO DEL PRECIO DEL ARROZ EN NOVIEMBRE
def prom_arr_grup_oct():
    c=-1
    promedio=0
    gr=op("Grupos")["Grupos_Revolico"][0]["Arroz"][0]["Octubre"]
    for i in range(30):
        c+=1
        promedio+=(gr[c]["CUP"])
    return(promedio//30)

#PROMERIO DEL PRECIO DEL FRIJOL EN OCTUBRE
def prom_frij_grup_nov():
    c=-1
    promedio=0
    gr=op("Grupos")["Grupos_Revolico"][0]["Frijoles"][0]["Noviembre"]
    for i in range(30):
        c+=1
        promedio+=(gr[c]["CUP"])
    return(promedio//30)

#PROMERIO DEL PRECIO DEL FRIJOL EN NOVIEMBRE
def prom_frij_grup_oct():
    c=-1
    promedio=0
    gr=op("Grupos")["Grupos_Revolico"][0]["Frijoles"][0]["Octubre"]
    for i in range(30):
        c+=1
        promedio+=(gr[c]["CUP"])
    return(promedio//30)