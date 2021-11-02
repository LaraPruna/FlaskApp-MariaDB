from flask import Flask
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
	if request.method=="GET":
		return render_template()
	user=request.form.get("usuario")
	pw=request.form.get("contraseña")
	return