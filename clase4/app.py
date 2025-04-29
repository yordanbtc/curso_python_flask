from flask import Flask, render_template
app = Flask(__name__)

@app.route("/for-loop")
def loop_for():
    equipos = [
            "REAL MADRID",
            "FC BARCELONA",
            "MILAN AC",
            "LIVERPOOL",
            "BAYERN MUNISH",
            "AJAX AMSTERD",
            "INTER MILAN",
            "JUVENTUS",
            "MANCHESTER UNITED",
            "OPORTO"
            ]
    
    return render_template("for_loop.html", teams = equipos)

if __name__=="__main__":
    app.run()