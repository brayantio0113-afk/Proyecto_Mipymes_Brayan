import matplotlib
from matplotlib import pyplot as plt
import Functions

#GRAFICA DE PIE QUE MUESTRA LA CANTIDAD Y PORCENTAJE DE METODOS DE PAGO QUE ACEPTAN LAS MIPYMES
def graf_pie_met_pago():
    cantidad=list(Functions.met_pago().values()) #ALMACENA LOS VALORES DEL DICC DE LOS METODOS DE PAGO
    cantidad.sort() #ORDENARLOS DE MAYOR A MENOR
    plt.figure(figsize=(15,15), facecolor="#f7f4ef") #ESTABLECE EL TAMAÑO DE LA VENTANA AL EJECUTARSE Y EL COLOR DE FONDO
    plt.pie(cantidad, #CREA LA GRAFICA DE PIE
            autopct="%1.0f%%", #AGREGA EL % QUE REPRESENTA CADA SECTOR
            colors=["#7a5195","#4f81bd", "#9bbb59", "#c0504d"], #PERSONALIZA LOS COLORES DE LOS SECTORES
            textprops={"fontsize":20, #AUMENTA EL TAMAÑO DEL TEXTO EN LOS SECTORES
                       "fontname":"algerian", #CAMBIA LA FUENTE DEL TEXTO EN LOS SECTORES
                       "color":"white", #CAMBIA EL COLOR DEL TEXTO EN LOS SECTORES
                       })
    
    plt.title("METODOS DE PAGO QUE ACEPTAN CADA UNA DE LAS MIPYMES", #CREA EL TITULO
              fontsize=25, #AUMENTA EL TAMAÑO
              fontname="algerian", #CAMBIA LA FUENTE
              fontweight="bold") #CONVIERTE EN NEGRITA
    plt.legend(["Euro: 2", "USD: 12","Cup: 30", "MLC: 30"], #CREA LA LEYENDA
               title="Tiendas que cumplen", #CREA EL TITULO DE LA LEYENDA
               fontsize=20, #AUMENTA EL TAMAÑO DE LOS VALORES DE LA LEYENDA
               title_fontsize=25, #AUMENTA EL TAMAÑO DEL TITULO DE LA LEYENDA
               bbox_to_anchor=(0.02, 0), #CAMBIA LA POSICION DEL CUADRO DE LEYENDA
               loc="lower right") #INDICA LA POSICION
    return (plt.show())

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
    plt.figure(figsize=(15,15), #ESTABLECE EL TAMAÑO DE LA VENTANA AL EJECUTARSE
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