from flask import Flask, render_template

app = Flask(__name__)
@app.route("/estructura")
def estructura_datos():
    peliculas = [
        "El lobo de wall street",
        "Harry Potter",
        "Volver al roues"
    ]
    return render_template("estructuras.html",movies=peliculas)


if __name__=="__main__":
    app.run()