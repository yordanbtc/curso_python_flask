from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://yordanbtc:2daDnmDE2F4gSNfG@tutorial.wxxqpk9.mongodb.net/")
app.db = cliente.ejemplo

usuarios = [usuario for usuario in app.db.usuarios.find({})]
#print (usuarios)

@app.route("/", methods = ["GET", "POST"])

def home():
    if request.method == "POST":
        info_formulario = request.form.get("contenido")
        parametros = {"nombre": info_formulario}
        usuarios.append(parametros)
        app.db.usuarios.insert_one(parametros)
        print(info_formulario)


    return render_template("formulario.html", usuarios = usuarios )


if __name__ == "__main__":
    app.run()