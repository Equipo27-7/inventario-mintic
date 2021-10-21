from flask import *
from . import db

main = Blueprint('main', __name__)

@main.route("/")  
def index():
    return render_template("index.html");  

@main.route("/dashboard", methods=['GET'])
def dashboard():  
    print('entro al Dashboard')
    return render_template("dashboard.html");  

@main.route("/usuario")  
def usuario():  
    return render_template("usuario.html");  

@main.route("/proveedor")  
def proveedor():  
    return render_template("proveedor.html");  

@main.route("/producto")  
def producto():  
    return render_template("producto.html");  
