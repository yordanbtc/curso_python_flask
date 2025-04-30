from flask import Flask, render_template
"""Estructuras de datos en Flask y Plantilla html? | Curso de Flask | E02"""

app = Flask(__name__)
class Pelicula: 
    def __init__(self, nombre, año, protagonista):
        self.nombre = nombre
        self.año = año
        self.protagonista = protagonista
        
@app.route("/estructura")
def estructura_datos():
    peliculas = [
        "El lobo de wall street",
        "Harry Potter",
        "Volver al futuro"
    ]

    lobo = {
        "Nombre" : "El lobo de wall street",
        "Año": "2013",
        "Protagonista" : "Leonardo DiCaprio"
    }

    volver = Pelicula(nombre="Volver al futuro", año="1985", protagonista="Michael J. Fox")

    return render_template("estructuras.html",movies=peliculas, destacada = lobo, favorita = volver)


if __name__=="__main__":
    app.run()