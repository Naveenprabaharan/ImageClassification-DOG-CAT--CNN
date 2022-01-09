from flask import Flask, render_template, request
import model as m

#Author Naveenprabaharan S - GCT[1918L12]

app = Flask(__name__)

@app.route("/" , methods = ["POST"])
def hello():
    if request.method == "POST":
        path = request.form['path']
        dogCAT_pred = m.DogCAT_pred(path)
        dcp = dogCAT_pred
        print(dcp)
        

    return render_template("index.html", pred = dcp , im_path=path)
    


@app.route("/") 
def submit():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)


"""
@app.route("/sub", methods = ["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form['username']

    # .py -> HTML
    return render_template("sub.html", n = name)
"""
