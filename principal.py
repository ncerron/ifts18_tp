#!/usr/bin/env python
from flask_bootstrap import Bootstrap
from flask import Flask, render_template,session, redirect, url_for
from formulario import MyLogin, MyRegistro
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
    users = leer_archivo.leer("passws.csv")
    return render_template('users.html', users=users)

@app.route('/')
@app.route('/index', methods=('GET', 'POST'))
def index():
    user2=leer_archivo.leer("passws.csv")
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
    user = leer_archivo.leer("passws.csv")
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
                leer_archivo.grabar("passws.csv", form.passw.data.strip(), form.usu.data.strip())
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

if __name__ == "__main__":
    app.run()
