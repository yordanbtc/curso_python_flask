from flask import Flask, render_template, request,redirect, url_for
import datetime
from pymongo import MongoClient

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://yordanbtc:2daDnmDE2F4gSNfG@tutorial.wxxqpk9.mongodb.net/")
app.db = cliente.blog


entradas=[entrada for entrada in app.db.contenido.find({})]
#print (entradas)

@app.route("/", methods =["GET", "POST"])

def home():
    if request.method == "POST":
        titulo = request.form.get("tit")
        entry = request.form.get("content")
        fecha_formato =datetime.datetime.today().strftime("%d-%m-%Y")
        parametros = {"titulo":titulo, "contenido": entry, "fecha": fecha_formato}
        entradas.append(parametros)
        app.db.contenido.insert_one(parametros)
        return redirect(url_for('home'))


    return render_template("index.html", entradas=entradas)

if __name__=="__main__":
    app.run()
