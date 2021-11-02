from flask import Flask, render_template, abort, request
import os, pymysql

app = Flask(__name__)
cursor = None

@app.route('/',methods=["GET"])
def login():
	return render_template("login.html")
	
@app.route('/buscador',methods=["POST"])
def buscador():
	conexion = pymysql.connect(
		host='192.168.1.108',
		user=request.form.get("usuario"),
		password=request.form.get("contraseña"),
		db='viajes')
	filtro=request.form.get("filtro")
	with conexion.cursor() as cursor:
		cursor.execute("SELECT Destino from Viajes")
		destinos = cursor.fetchall()
	conexion.close()
	return render_template("buscador.html",filtro=filtro,destinos=destinos)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)