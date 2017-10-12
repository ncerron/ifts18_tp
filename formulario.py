from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
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
