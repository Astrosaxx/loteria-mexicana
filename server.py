from flask import Flask, render_template
import random

app = Flask(__name__)

#TODO Lista de cartas
cartas_loteria = [
    "1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas", "6  La sirena",
    "7  La escalera", "8  La botella", "9  El barril", "10 El árbol", "11 El melón", "12 El valiente",
    "13 El gorrito", "14 La muerte", "15 La pera", "16 La bandera", "17 El bandolón", "18 El violoncello",
    "19 La garza", "20 El pájaro", "21 La mano", "22 La bota", "23 La luna", "24 El cotorro", "25 El borracho",
    "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón", "31 Las jaras",
    "32 El músico", "33 La araña", "34 El soldado", "35 La estrella", "36 El cazo", "37 El mundo",
    "38 El apache", "39 El nopal", "40 El alacrán", "41 La rosa", "42 La calavera", "43 La campana",
    "44 El cantarito", "45 El venado", "46 El sol", "47 La corona", "48 La chalupa", "49 El pino",
    "50 El pescado", "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"
]

def generar_cartas_aleatorias(cantidad):
    #* Genera una lista aleatoria de cartas con duplicados si es necesario.
    total_disponibles = len(cartas_loteria)

    # Repetir las cartas hasta cubrir la cantidad necesaria
    repeticiones = (cantidad // total_disponibles) + 1
    cartas_repetidas = cartas_loteria * repeticiones

    # Mezclar y recortar exactamente la cantidad necesaria
    cartas_seleccionadas = random.sample(cartas_repetidas, cantidad)
    return cartas_seleccionadas


#* Primer endpoint para la lotería
@app.route("/loteria")
def loteria_default():
    filas, columnas = 4, 4
    total_cartas = filas * columnas
    cartas = generar_cartas_aleatorias(total_cartas)
    return render_template("tablero.html", filas=filas, columnas=columnas, cartas=cartas)

#* Endpoint para la lotería con un número de filas
@app.route("/loteria/<int:x>")
def loteria_filas(x):
    filas = x
    columnas = 4
    if filas <= 0:
        return "El número de filas debe ser mayor que cero.", 400
    total_cartas = filas * columnas
    cartas = generar_cartas_aleatorias(total_cartas)
    return render_template("tablero.html", filas=filas, columnas=columnas, cartas=cartas)

#* Endpoint para la lotería con un número de filas y columnas
@app.route("/loteria/<int:x>/<int:y>")
def loteria_filas_columnas(x, y):
    total_cartas = x * y
    cartas = generar_cartas_aleatorias(total_cartas)
    return render_template("tablero.html", filas=x, columnas=y, cartas=cartas)

if __name__ == "__main__":
    app.run(debug=True)
