from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def home():
    info_formulario = ""
    if request.method == "POST":
        info_formulario = request.form.get("contenido")
        print("Hola "+info_formulario)
    return render_template("formulario.html", nombre = info_formulario )


if __name__ == "__main__":
    app.run()