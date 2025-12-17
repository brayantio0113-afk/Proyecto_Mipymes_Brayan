import matplotlib
from matplotlib import pyplot as plt
import Functions

#GRAFICA DE PIE QUE MUESTRA LA CANTIDAD DE MIPYMES EN LAS QUE SE PUEDEN COMPRAR LOS 10 PRODUCTOS CON EL SALARIO PROMEDIO
def graf_pie_salario():
    cumple=list(Functions.alc_salario().keys())
    cantidad=list(Functions.alc_salario().values())
    plt.pie(cantidad, autopct="%1.0f%%", colors=["#c52233","#3f37c9"], textprops={"fontsize":30, "fontname":"algerian", "color":"white", "fontweight":"bold"})
    plt.title("TIENDAS DONDE SE PUEDEN COMPRAR LOS 10 PRODUCTOS CON EL SALARIO PROMEDIO (5839)", fontsize=25, fontname="algerian")
    plt.legend(["Si: 10", "No: 20"], title="Tiendas que cumplen", fontsize=30, title_fontsize=30, bbox_to_anchor=(0.02, 0),loc="lower right")
    return (plt.show())