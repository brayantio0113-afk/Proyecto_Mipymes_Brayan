import Functions
import matplotlib.pyplot as plt
from Open_json import op
#GRAFICA DE BARRAS HORIZONRAL QUE MUESRA LA FRECUENCIA CON QUE SE ENCUENTRA CADA PRODUCTO EN LAS MIPYMES
def graf_cant_prod():
    cant_prod=Functions.cantidad_productos() #ALMACENA EL DICC DE LA CANTIDAD DE PRODUCTOS
    cant_prod_ord=dict(sorted(dict.items(cant_prod), key=lambda item: item[1])) #ORDENA EL DICC POR VALORES DE MENOR A MAYOR
    productos=list(cant_prod_ord.keys()) #ALMACENA LAS LLAVES DEL DICC
    cantidad=list(cant_prod_ord.values()) #ALMACENA LOS VALORES DEL DICC
    productos_pos=[] #LISTA VACIA PARA EXTRAER LOS INDICES DE LA LISTA DE LAS LLAVES
    for i in range(len(productos)): #AÑADE LOS INDICES A LA LISTA
        productos_pos.append(i)
    productos_upp=[i.upper() for i in productos] #PONE LAS LLAVES EN MAYUSCULAS
    plt.figure(figsize=(15,10), #ESTABLECE EL TAMAÑO DE LA VENTANA AL EJECUTARSE
               facecolor="#f2f2f2") #CAMBIA EL COLOR DEL FONDO
    plt.barh(productos_upp, cantidad, # CREA EL GRAFICOS DE BARRA HORIZONTAL
            height=0.8, #ESTABLECE EL ANCHO DE LAS BARRAS
            color="#0547ef") #CAMBIA EL COLOR DE LAS BARRAS
    plt.subplots_adjust(left=0.15, right=0.9, top=0.95, bottom=0.03) #AJUSTA EL TAMAÑO DE LA GRAFICA
    plt.ylim(-1,57) #AJUSTA EL LIMITE MIN Y MAX EN EL EJE Y
    plt.xlim(0, 25) #AJUSTA EL LIMITE MIN Y MAX EN EL EJE X
    plt.yticks(fontsize=7.5, #CAMBIA EL TAMAÑO DE LOS TICKS DEL EJE Y
            fontweight="bold") #PONE LOS TICKS EN NEGRITA
    plt.xticks(cantidad, #ESTABLECE LOS TICKS EN EL EJE X
            fontsize=10, #ESTABLECE EL TAMAÑO DE LOS TICKS DEL EJE X
            fontweight="bold") #PONE LOS TICKS DEL EJE X EN NEGRITA
    plt.title("FRECUENCIA DE LOS PRODUCTOS POR MIPYME", #ESTABLECE EL TITULO 
            fontsize=20, #CAMBIA EL TAMAÑO DEL TITULO
            fontname="algerian") #CAMBIA LA FUENTE DEL TITULO
    for pr, ca in zip(productos_pos, cantidad): #TRAZA LINEAS DESDE EL FINAL DE CADA BARRA HASTA EL EJE X
        plt.vlines(x=ca, ymin=pr - 60, ymax=pr + 0.3, color="red", linestyles="--", linewidth=1)
    return (plt.show())

#GRÁFICA QUE MUESTRA LA COMPARATIVA DE LA VARIACION DE LOS PRECIOS DEL USD Y EURO EN EL TOQUE
def graf_pl_ElToque():
    price_usd=Functions.usd() #ALMACENA LOS VALORES DEL USD
    price_euro=Functions.euro() #ALMACENA LOS VALORES DEL EURO
    price_mlc=Functions.mlc() #ALMACENA LOS VALORES DEL MLC
    fechas=Functions.id_eltoque() #ALMACENA LOS ID DE LOS DIAS DE ANÁLISIS DE ELTOQUE
    plt.figure(figsize=(15,5), #ESTABLECE EL TAMAÑO DE LA FIGURA
            facecolor=("#f7f4ef")) # ESTABLECE EL COLOR DE FONDO
    plt.plot(fechas, price_euro, #CREA UNA GRÁFICA DE LINEAS
            marker=".", #CREA UN MARCADOR EN CADA VALOR DE LA GRÁFICA
            color="blue") #CAMBIA EL COLOR DE LA LÍNEA
    plt.plot(fechas, price_usd, #CREA OTRA LÍNEA EN LA MISMA GRÁFICA
            marker=".", 
            color="green")
    plt.xlim (0,62) #ESTABLECE EL LÍMITE DEL EJE X
    leyenda=plt.legend(["Euro", "USD"], #CREA UNA LEYENDA
                title="MONEDAS", #CREA UN TÍTULO PARA LA LEYENDA
                title_fontsize=15, #CAMBIA EL TAMAÑO DEL TITULO DE LA LEYENDA
                prop={"family":"algerian", #CAMBIA LA FUENTE DEL TEXTO EN LA LEYENDA
                    "size":15},) #CAMBIA EL TAMAÑO DEL TEXTO EN LA LEYENDA
    plt.title("COMPARACIÓN DE LA VARIACIÓN DE LOS PRECIOS DEL USD Y EL EURO POR ELTOQUE", #ESTABLECE UN TÍTULO A LA GRÁFICA
            fontname="algerian", #CAMBIA LA FUENTE DEL TEXTO DEL TÍTULO
            fontsize=20) #CAMBIA EL TAMAÑO DEL TEXTO DEL TÍTULO
    plt.setp(leyenda.get_title(), fontfamily='algerian', fontsize=16, fontweight='bold') #MODIFICA EL TEXTO EN EL TÍTULO DE LA LEYENDA
    plt.ylim(400, 550) #ESTABLECE EL LÍMITE DEL EJE Y
    plt.xticks(fechas, #CREA LOS VALORES DEL EJE X
            fontsize=8) #CAMBIA EL TAMAÑO DEL TEXTO DE LOS VALORES DEL EJE X
    plt.xlabel("DIAS DE ANÁLISIS", #CREA UN TÍTULO PARA EL EJE X
            fontname="algerian",
            fontsize=20)
    plt.ylabel("PRECIOS EN CUP", #CREA UN TÍTULO PARA EL EJE Y
            fontname="algerian",
            fontsize=20)
    for i, k in zip(price_euro,fechas ):
            plt.vlines(x=k, ymin=i - 200, ymax=i - 1, color="red", linestyles="--", linewidth=0.5) #CREA LÍNNEAS QUE VAN DESDE EL PUNTO EN CADA VALOR HASTA EL EJE X
    return(plt.show())

#GRAFICA DE BARRAS DOBLES QUE COMPARA LOS PRECIOS DEL USD Y EL ACEITE EN LOS MESES DE OCTUBRE Y NOVIEMBRE
def graf_bar_comp_usd_ac():
    usd_et_nov=Functions.prom_nov_et(Functions.usd()) #ALMACENA EL PRECIO PROMEDIO DEL USD EN NOVIEMBRE
    usd_et_oct=Functions.prom_oct_et(Functions.usd()) #ALMACENA EL PRECIO PROMEDIO DEL USD EN OCTUBRE
    ac_nov=Functions.prom_ac_grup_nov() #ALMACENA EL PRECIO PROMEDIO DEL ACEITE EN NOVIEMBRE
    ac_oct=Functions.prom_ac_grup_oct() #ALMACENA EL PRECIO PROMEDIO DEL ACEITE EN OCTUBRE
    arr_nov=Functions.prom_arr_grup_nov()
    arr_oct=Functions.prom_arr_grup_oct()
    frij_nov=Functions.prom_frij_grup_nov()
    frij_oct=Functions.prom_frij_grup_oct()
    plt.figure(figsize=(8,8),
               facecolor="#f7f4ef")
    plt.bar(0.9, ac_oct, width=0.30, color="blue", edgecolor="black") #ESTAS 4 LÍNEAS CREAN 4 BARRAS EN 2 VALORES DEL EJE X, 2 EN CADA VALOR QUE SON LOS PROMEDIOS DEL ACEITE
    plt.bar(0.6, ac_nov, width=0.30, color="red", edgecolor="black") #Y LOS PROMEDIOS DEL USD, LAS 2 BARRAS EN CADA VALOR SON LOS PROMEDIOS EN OCTUBRE Y EN NOVIEMBRE RESPECTIVAMENTE 
    plt.bar(0.15, usd_et_oct, width=0.30, color="blue", edgecolor="black") #DEL ACEITE Y EL USD
    plt.bar(-0.15, usd_et_nov, width=0.30, color="red", edgecolor="black")
    plt.bar(1.65, arr_nov, width=0.30, color="blue", edgecolor="black")
    plt.bar(1.35, arr_oct, width=0.30, color="red", edgecolor="black")
    plt.bar(2.10, frij_nov, width=0.30, color="red", edgecolor="black")
    plt.bar(2.40, frij_oct, width=0.30, color="blue", edgecolor="black")
    plt.legend(["NOVIEMBRE", "OCTUBRE"], fontsize=15) 
    plt.xticks([0,0.75, 1.5, 2.25], ["USD", "ACEITE", "ARROZ", "FRIJOLES"], fontname="algerian", fontsize=20) #ESTABLECE LOS VALORES DEL EJE X Y MODIFICA EL TEXTO
    plt.text(0.9, ac_oct, ac_oct, ha="center", va="bottom", fontweight="bold") #ESTAS 4 LÍNEAS CREAN UN TEXTO ENCIMA DE CADA BARRA CON EL NÚMERO DEL PROMEDIO DE CADA UNA
    plt.text(0.6, ac_nov, ac_nov, ha="center", va="bottom", fontweight="bold") #Y MODIFICA EL TIPO DE LETRA
    plt.text(0.15, usd_et_oct, usd_et_oct, ha="center", va="bottom", fontweight="bold")
    plt.text(-0.15, usd_et_nov, usd_et_nov, ha="center", va="bottom", fontweight="bold")
    plt.text(1.35, arr_oct, arr_oct, ha="center", va="bottom", fontweight="bold")
    plt.text(1.65, arr_nov, arr_nov, ha="center", va="bottom", fontweight="bold")
    plt.text(2.10, frij_nov, frij_nov, ha="center", va="bottom", fontweight="bold")
    plt.text(2.40, frij_oct, frij_oct, ha="center", va="bottom", fontweight="bold")
    plt.yticks(fontname="algerian", fontsize=15) #ESTABLECE LOS VALORES DEL EJE Y Y MODIFICA EL TEXTO
    plt.title("COMPARACIÓN DE LOS PROMEDIOS DEL USD Y EL ACEITE EN LOS MESES DE OCTUBRE Y NOVIEMBRE", fontname="algerian", fontsize=20)
    return (plt.show())

#GRAFICA DE PIE QUE MUESTRA EN CUANTAS MIPYMES ALCANZA PARA COMPRAR LOS PRODUCTOS
def graf_pie_alc_salario():
    alcanza=list(Functions.alc_salario_dic().values()) #ALMACENA LOS VALORES DEL DICC DEL SALARIO
    lista_mipymes=[]
    sumas=list(Functions.alc_salario_nombres_dicc().values())
    c=0
    for i in list(Functions.alc_salario_nombres_dicc().keys()):
        precio=sumas[c]
        lista_mipymes.append(f"{i}: {precio}")
        c+=1
    nombres = "\n".join(lista_mipymes)
    plt.figure(figsize=(8,8), facecolor="#f7f4ef") #ESTABLECE EL TAMAÑO DE LA VENTANA AL EJECUTARSE Y EL COLOR DE FONDO
    plt.pie(alcanza, #CREA LA GRAFICA DE PIE
            autopct="%1.0f%%", #AGREGA EL % QUE REPRESENTA CADA SECTOR
            colors=["#4f81bd","#bb0600"], #PERSONALIZA LOS COLORES DE LOS SECTORES
            textprops={"fontsize":30, #AUMENTA EL TAMAÑO DEL TEXTO EN LOS SECTORES
                       "fontname":"algerian", #CAMBIA LA FUENTE DEL TEXTO EN LOS SECTORES
                       "color":"white", #CAMBIA EL COLOR DEL TEXTO EN LOS SECTORES
                       })
    
    plt.title("Mipymes en las que se puede comprar una unidad de cada uno de los 10 productos con el salario basico (5849cup)", #CREA EL TITULO
              fontsize=18, #AUMENTA EL TAMAÑO
              fontname="algerian", #CAMBIA LA FUENTE
              fontweight="bold", #CONVIERTE EN NEGRITA
              loc="center")
    plt.legend(Functions.alc_salario_dic().items(), #CREA LA LEYENDA
               title="Tiendas que cumplen", #CREA EL TITULO DE LA LEYENDA
               fontsize=25, #AUMENTA EL TAMAÑO DE LOS VALORES DE LA LEYENDA
               title_fontsize=25, #AUMENTA EL TAMAÑO DEL TITULO DE LA LEYENDA
               bbox_to_anchor=(0.02, 0), #CAMBIA LA POSICION DEL CUADRO DE LEYENDA
               loc="lower right") #INDICA LA POSICION
    plt.text(
    1.05, 0.5,
    nombres,
    transform=plt.gca().transAxes,
    fontsize=12,
    fontname="algerian",
    va="center"
)

    return (plt.show())
#GRAFICA DE SCATTER QUE MUESTRA LOSMETODOS DE PAGO ACEPTADOS POR MIPYME
def graf_scatter_metodos_pago():
    dicc=Functions.met_pago_dicc()
    monedas = ["CUP", "USD", "MLC", "Euro"]
    mipymes = list(dicc.keys())

    # Mapear categorías a números
    x_map = {moneda: i for i, moneda in enumerate(monedas)}
    y_map = {mipyme: i for i, mipyme in enumerate(mipymes)}

    x_vals = []
    y_vals = []

    for mipyme, monedas_aceptadas in dicc.items():
        for moneda in monedas_aceptadas:
            if moneda in x_map:
                x_vals.append(x_map[moneda])
                y_vals.append(y_map[mipyme])

    plt.figure(figsize=(10,8),
               facecolor="#f7f4ef")
    plt.scatter(x_vals, y_vals,
                s=100,
                color="#910404",
                facecolor="#5500FF")
    plt.xticks(
        ticks=range(len(monedas)),
        labels=monedas,
        fontname="algerian",
        fontsize=15
    )
    plt.yticks(
        ticks=range(len(mipymes)),
        labels=mipymes,
        fontname="algerian"
    )
    plt.xlabel("Monedas aceptadas",
               fontname="algerian",
               fontsize=25,)
    plt.ylabel("Mipymes",
               fontname="algerian",
               fontsize=25)
    plt.title("Métodos de pago aceptados por mipyme", 
              fontname="algerian",
              fontsize=25)
    plt.xlim(-1,4)

    plt.grid(True, color="#5500FF")
    plt.tight_layout()
    return plt.show()