from flask import *
from flask_login import login_required, current_user, login_user, logout_user
from . import db

main = Blueprint('main', __name__)

@main.route("/")  
def index():
    return render_template("index.html");  

@main.route("/dashboard", methods=['GET'])
@login_required
def dashboard():  
    return render_template("dashboard.html", name=current_user.nombre, rol = current_user.rol_id);  

@main.route("/usuario") 
@login_required 
def usuario():  
    return render_template("usuario.html");  

@main.route("/proveedor") 
@login_required 
def proveedor():  
    return render_template("proveedor.html");  

@main.route("/producto")  
@login_required
def producto():  
    return render_template("producto.html");  
