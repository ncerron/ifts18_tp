from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms import validators

class MyLogin(FlaskForm):
    """se especifica los campos que tendra el formulario, el cual se usara en la funcion login() del archivo
     principal.py """
    usu = StringField('Usuario', [validators.data_required(message = "Debe ingresar un usuario")])
    passw = PasswordField('Login', [validators.data_required(message = "Debe ingresar una contraseña")])
    submit = SubmitField("Ingresar")

class MyRegistro(FlaskForm):
    """se establece los campos que tendra el formulario en la funcion registro() el archivo
     principal.py """
    usu = StringField('Usuario', [validators.data_required(message = "Debe ingresar un usuario")])
    passw = PasswordField('Contraseña', [validators.data_required(message = "Debe ingresar una contraseña")])
    usu1 = StringField('Repetir Usuario', [validators.data_required(message = "Debe ingresar un usuario ")])
    passw1 = PasswordField('Repetir Contraseña', [validators.data_required(message = "Debe ingresar una contraseña")])
    submit = SubmitField("Enviar")

class MyConsultaCliente(FlaskForm):
    """se establece los campos que tendra el formulario en la funcion cliente() el archivo
     principal.py """
    submit = SubmitField("Buscar")
    cliente = StringField('Cliente', [validators.data_required(message = "Debe ingresar el nombre del Cliente"), validators.Length(min = 3, message = "Debe ingresar como minimo 3 caracteres")])
    submit_selec = SubmitField("Seleccionar")

class MyConsultaProducto(FlaskForm):
    """se establece los campos que tendra el formulario en la funcion producto() el archivo
     principal.py """
    submit = SubmitField("Buscar")
    producto = StringField('Producto', [validators.data_required(message = "Debe ingresar el nombre del Producto"), validators.Length(min = 3, message = "Debe ingresar como minimo 3 caracteres")])
    submit_selec = SubmitField("Seleccionar")

class MyConsulta(FlaskForm):
    """se establece los campos que tendra el formulario en la funcion mejores_clientes() y mas_vendidos() el archivo
     principal.py """
    submit = SubmitField("Aceptar")
    cantidad = IntegerField('Cantidad de items a mostrar', [validators.data_required(message = "Debe ingresar un numero entero")])