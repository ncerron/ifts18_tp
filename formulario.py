from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms import validators

class MyLogin(FlaskForm):

    usu = StringField('Usuario', [validators.data_required(message="Debe ingresar Usuario")])
    ##validator es una lista en donde todas las validaciones que quiero que se cumplan

    passw = PasswordField('Login', [validators.data_required(message="Debe ingresar Login")])
    submit = SubmitField("Ingresar")

class MyRegistro(FlaskForm):

    usu = StringField('Usuario', [validators.data_required(message="Debe ingresar Usuario")])
    passw = PasswordField('Contraseña', [validators.data_required(message="Debe ingresar Login")])
    usu1 = StringField('Repetir Usuario', [validators.data_required(message="Debe ingresar Usuario")])
    passw1 = PasswordField('Repetir Contraseña', [validators.data_required(message="Debe ingresar Login")])
    submit = SubmitField("Enviar")


class MyCliente(FlaskForm):
    submit = SubmitField("Confirmar")
    archivo= SelectField('Seleccione un archivo:', choices=[("archivo.csv", "archivo"), ("arch_codigo_vacio.csv", "arch_codigo_vacio"),("arch_datoinvalido.csv", "arch_datoinvalid")])