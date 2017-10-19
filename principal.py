#!/usr/bin/env python
from flask_bootstrap import Bootstrap
from flask import Flask, render_template,session, redirect, url_for
from formulario import MyLogin, MyRegistro, MyCliente
import leer_archivo

app = Flask(__name__)
app.config["SECRET_KEY"]= "String dificil de adivinar"
bootstrap = Bootstrap(app)

@app.route('/bienvenido')
def bienvenido():
    # se borra la sesion al clickear logout
    session.pop('nombre', None)
    return redirect(url_for('index'))

@app.route('/users', methods=('GET', 'POST'))
def user():
    users = leer_archivo.leer("archivos_csv/passws.csv")
    return render_template('users.html', users=users)

@app.route('/')
@app.route('/index', methods=('GET', 'POST'))
def index():
    user2=leer_archivo.leer("archivos_csv/passws.csv")
    form2 = MyLogin()
    if form2.validate_on_submit():
        for l in user2:
            if l['usuario']==form2.usu.data.strip():
               if l['login'] == form2.passw.data.strip():
                   session['nombre'] = form2.usu.data.strip()
                   return render_template('bienvenido.html', form=form2, usuario= form2.usu.data.strip())
               else:
                   #coincide usuario pero no el login
                   form2.passw.data = " "
                   return render_template('index.html', form=form2, msj="ok")
        form2.passw.data = " "
        form2.usu.data = " "
        return render_template('index.html', form=form2, msj=" " )
    return render_template('index.html', form  =form2)

@app.route('/registro', methods=('GET', 'POST'))
def registro():
    user = leer_archivo.leer("archivos_csv/passws.csv")
    form = MyRegistro()
    registrado = True
    if form.validate_on_submit():
        for l in user:
            if l['usuario'] == form.usu.data.strip():
                #usuario se encuentra registrado
                form.passw1.data = " "
                form.usu1.data = " "
                form.passw.data= " "
                form.usu.data= " "
                return render_template('registro.html', form=form, msj="reg")
            else:
                 registrado=False
        if form.passw1.data.strip() == form.passw.data.strip() and form.usu1.data.strip()==form.usu.data.strip():
            if registrado == False:
                leer_archivo.grabar("archivos_csv/passws.csv", form.passw.data.strip(), form.usu.data.strip())
                #registro exitoso
                form.passw1.data = " "
                form.usu1.data = " "
                form.passw.data = " "
                form.usu.data = " "
                return render_template('registro.html', form=form, msj="ok")
        else:
            #verifique datos ingresados
            form.passw1.data = " "
            form.usu1.data = " "
            form.passw.data = " "
            form.usu.data = " "
            return render_template('registro.html', form=form, msj=" ")
    return render_template('registro.html', form  =form)

@app.route('/clientes', methods=('GET', 'POST'))
def clientes():
    form=MyCliente()
    if form.validate_on_submit():
        f="archivos_csv/" + form.archivo.data
        f_rta=leer_archivo.leer_validar(f)
        if f_rta:
            clientes=leer_archivo.leer(f)
            return render_template('clientes.html', form=form, clientes=clientes, ff=True)
        else:
            return render_template('clientes.html', form=form,  ff=False, msg= form.archivo.data + " no se puede procesar")

    return render_template('clientes.html', form= form, ff=False)

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()
