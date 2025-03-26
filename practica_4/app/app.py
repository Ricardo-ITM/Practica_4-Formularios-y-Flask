from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def inicio():
	return render_template("public/index.html")

@app.route("/sobremi")
def sobremi():
	return render_template("public/sobre.html")

@app.route("/contacto")
def contacto():
	return render_template("public/contacto.html")

@app.route("/blog")
def blog():
	return render_template("public/blog.html")

@app.route("/portafolio")
def portafolio():
	return render_template("public/portafolio.html")