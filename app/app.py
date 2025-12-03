#from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerEstadosTarea import *
from controller.controllerProyectos import *
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
application = app

@app.route('/', methods=['GET', 'POST'])
def inicio_view():
    return render_template('public/layout.html', miData=listaEstadosTarea())


@app.route('/listar', methods=['GET', 'POST'])
def saludo_view():
    return render_template('public/listarEstadosTareas.html', miData=listaEstadosTarea())

@app.route('/listaproyectos', methods=['GET', 'POST'])
def listarProyectos_view():
    return render_template('public/listarProyectos.html', miData=listaProyecto())

@app.route('/agregarproyecto', methods=['GET', 'POST'])
def agregarproyecto_view():
    return render_template('public/agregarProyecto.html')

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio_view'))

if __name__ == "__main__":
    app.run(debug=True, port=8000)


