from flask import Flask, render_template
app = Flask(__name__)

@app.route("/condicionales")
def condicional():
    return render_template("condicional.html", equipo = "Inter")




if __name__=="__main__":
    app.run()