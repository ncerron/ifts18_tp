#!/usr/bin/env python
from flask_bootstrap import Bootstrap
from flask import Flask, render_template,session, redirect, url_for, request, flash
from formulario import MyLogin, MyRegistro, MyConsultaCliente, MyConsultaProducto, MyConsulta
import archivo

app = Flask(__name__)
app.config["SECRET_KEY"] = "String dificil de adivinar"
bootstrap = Bootstrap(app)

@app.route("/logout")
def logout():
    """funcion para salir de la sesion generada al ingresar a traves de la pagina login"""
    session.pop('nombre', None)
    return redirect(url_for('index'))


@app.route("/users", methods = ('GET', 'POST'))
def user():
    """listado de usuarios creados, solo se puede ver si el usuario que ingreso a la sesion es admin"""
    if session.get("nombre"):
        users = archivo.leer("archivos_csv/passws.csv")
        return render_template('users.html', users = users)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))


@app.route("/login", methods = ('GET', 'POST'))
def login():
    """Aqui se realiza el logueo del usuario, se valida si el usuario se encuentra registrado comparando los datos
     ingresados en la pagina con con los datos de usuarios registrados que contiene el archivo passws.csv, esta info es
     asignada  a la variable user2. Si el usuario ingresado es admin, se redigira a la pagina ventas, sino a la pagina
     usuario"""
    user2 = archivo.leer("archivos_csv/passws.csv")
    form2 = MyLogin()
    if form2.validate_on_submit():
        for l in user2:
            if l['usuario'] == form2.usu.data.strip():
                if l['login'] == form2.passw.data.strip():
                    session["nombre"] = form2.usu.data.strip()
                    ## se establece un nombre a la sesion
                    if session["nombre"] == "admin":
                        return redirect(url_for('ventas'))
                    else:
                        return redirect(url_for('usuario'))
                else:
                    form2.passw.data = ""
                    # a traves de la variable msj, en html se informa que se verifique la contraseña
                    return render_template('login.html', form = form2, msj = "ok")
        form2.passw.data = ""
        form2.usu.data = ""
         ##a traves de la variable msj, en html se informa usuario no encontrado
        return render_template("login.html", form=form2, msj="mal")
    return render_template("login.html", form = form2)


@app.route("/")
@app.route("/index", methods = ('GET', 'POST'))
def index():
    """pagina de bienvenida al iniciar la aplicacion"""
    if not session.get("nombre"):
       return render_template('index.html')
    return redirect(url_for('login'))


@app.route("/registro", methods = ('GET', 'POST'))
def registro():
    """Aqui se realiza la registracion de nuevos usuarios, se valida si el usuario se encuentra registrado comparando
    los datos ingresados en la pagina con con los datos de usuarios registrados que contiene el archivo passws.csv, esta
     info es asignada  a la variable user, luego de esta validacion se comparan que coincidan los campos que hacen
     refencia al nombre y contraseñaa del nuevo usuario, si esto es afirmativo, se procedera a grabar los datos en el
     arhivo passws.csv"""
    def limpiar():
        #limpieza de los campos de la pagina
        form.passw1.data = " "
        form.usu1.data = " "
        form.passw.data = " "
        form.usu.data = " "
    user = archivo.leer("archivos_csv/passws.csv")
    form = MyRegistro()
    registrado = True
    if form.validate_on_submit():
        for l in user:
            if l['usuario'] == form.usu.data.strip():
                limpiar()
                # a traves de la vairable msj, en html se informa que usuario se encuentra registrado
                return render_template('registro.html', form = form, msj="reg")
            else:
                 registrado = False
        if form.passw1.data.strip() == form.passw.data.strip():
            if form.usu1.data.strip() == form.usu.data.strip():
                if registrado == False:
                    archivo.grabar("archivos_csv/passws.csv", form.passw.data.strip(), form.usu.data.strip())
                    limpiar()
                    # a traves de la variable msj, en html se informa la registracion exitosa
                    return render_template('registro.html', form = form, msj = "ok")
            else:
                # a traves de la variable usu, en html se muestra mensaje indicando que no coinciden los usuarios ingresados
                return render_template('registro.html', form=form, msj="usu")
        else:
            # a traves de la variable msjn en html se muestra mensaje indicando que no coinciden las contraseñas ingresadas
            return render_template('registro.html', form=form, msj="pass")
    return render_template('registro.html', form  = form)


@app.route("/ventas")
def ventas():
    """Pagina de bienvenida para el usuario logueado admnin"""
    if session.get("nombre"):
        clientes = archivo.leer("archivos_csv/archivo.csv")
        ## se valida el archivo, si fue exitosa, a traves de ff se muestra la info de la variable clientes
        return render_template('ventas.html', clientes = clientes, usuario = session.get('nombre'), ff = True)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))


@app.route("/usuario")
def usuario():
    """Pagina de bienvenida para el usuario logueado que NO es admin"""
    usuario = session['nombre']
    return render_template('usuario.html', usuario = usuario)


@app.route("/cliente", methods = ('GET', 'POST'))
def cliente():
    """Funciona junto con la pagina mostrar para listar todos los productos que compro un cliente, en esta pagina el
    usuario debe ingresar 3 caracteres que componen el nombre del cliente a buscar, como resultado se obtendra una lista
    de posibles clientes, en la cual el usuario debe elegir uno de ellos, y al clickear el boton seleccionar se
    redireccionara a la pagina mostrar, en donde se visualizara el listado"""
    if session.get("nombre"):
        form = MyConsultaCliente()
        lista_busqueda = archivo.lista_clientes("archivos_csv/archivo.csv")
        ff = False
        msg = ""
        if form.validate_on_submit():
            lista = []
            if form.cliente.data != None:
                for palabra in lista_busqueda:
                    if form.cliente.data.upper() in palabra:
                        lista.append(palabra)
                if len(lista) != 0:
                    ff = True
                else:
                    ff = False
                    msg = "No se encontro nombre del cliente"
                    # ff habilita la visualizacion del contenido de la variable lista
                return render_template("cliente.html", form = form, lista = lista, msg = msg , ff = ff)
        return render_template("cliente.html", form = form, ff = False)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))


@app.route("/producto", methods = ('GET', 'POST'))
def producto():
    """ Funciona junto con la pagina mostrar para listar todos los clientes que compraron un  determinado producto, en
    esta pagina el usuario debe ingresar 3 caracteres que componen el nombre del producto a buscar, como resultado se
    obtendra una lista de posibles productos, en la cual el usuario debe elegir uno de ellos, y al clickear el boton
    seleccionar se redireccionara a la pagina mostrar, en donde se visualizara el listado"""
    if session.get("nombre"):
        form = MyConsultaProducto()
        lista_busqueda = archivo.lista_producto("archivos_csv/archivo.csv")
        ff = False
        msg = ""
        if form.validate_on_submit():
            lista = []
            if form.producto.data != None:
                for palabra in lista_busqueda:
                    if form.producto.data.upper() in palabra:
                        lista.append(palabra)
                if len(lista) != 0:
                    ff = True
                else:
                    ff = False
                    msg = "No se encontro nombre del producto"
                    # ff habilita la visualizacion del contenido de la variable lista
                return render_template('producto.html', form = form, lista = lista, msg = msg , ff = ff)
        return render_template('producto.html', form = form, ff = False)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

@app.route("/mostrar", methods=('GET', 'POST'))
def mostrar():
    """En base al nombre seleccionado en las paginas cliente o producto, se genera el listado correspondiente, el mismo
    se visualizara en esta misma pagina"""
    if session.get("nombre"):
        if request.method == 'POST':
            lista = []
            msg = ""
            msg2 = ""
            msg3 = ""
            listado = archivo.leer("archivos_csv/archivo.csv")
            seleccion = request.form['selecc']
            for l in listado:
                if seleccion == l['CLIENTE']:
                    msg = "Listado de todos los productos que compro un Cliente"
                    msg2 = seleccion
                    msg3 = "cliente"
                    lista.append(l)
                elif seleccion == l['PRODUCTO']:
                    lista.append(l)
                    msg = "Listado de clientes que comparon un producto"
                    msg2 = seleccion
                    msg3 = "producto"
                    # ff habilita la visualizacion del contenido de la variable lista junto con msg y msg3
                    # la variable msg3 es utilizada para volver al html en donde se origino la solicitud
            return render_template('mostrar.html', lista=lista, ff=True, msg=msg, msg2=msg2, msg3=msg3)
        return render_template('mostrar.html')
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))


@app.route("/mejores_clientes", methods = ('GET', 'POST'))
def mejores_clientes():
    """En esta pagina se generara y visualizara el listado de los clientes que realizaron la mayor cantidad de compras,
     para realizar esto se necesita:
      l- a cantidad de clientes que se quiere mostrar, el usuario ingresara este dato.
      2- la informacion de las ventas se obtiene del archivo archivo.csv, el cual sera leido y asignados los datos en la
         variable listado.
      3- la  variable lista_busqueda en la cual se asigna el listado de clientes sin duplicados que contiene el archivo
         archivo.csv.
      Primero se genera una lista que contiene el nombre del cliente y cuanto gasto, y luego con ella se genera otra
      lista con la cantidad de items que pide el usuario, se la ordena para que los valores sean visualizados en forma
      descendente."""
    if session.get("nombre"):
        form = MyConsulta()
        if form.validate_on_submit():
            listado = archivo.leer("archivos_csv/archivo.csv")
            masgasto = []
            consulta = []
            lista_busqueda = archivo.lista_clientes("archivos_csv/archivo.csv")
            for listcli in lista_busqueda:
                gastoTotal = 0
                for clientes in listado:
                    if listcli == clientes['CLIENTE']:
                        gasto = float(clientes['CANTIDAD']) * float(clientes['PRECIO'])
                        gastoTotal = gastoTotal + gasto
                masgasto.append([gastoTotal, listcli])
            cont = 1
            masgasto.sort(reverse = True)
            for datos in masgasto:
                if cont <= form.cantidad.data:
                    consulta.append(datos)
                    cont = cont + 1
            consulta.sort(reverse = True)
            ## ver variables fc y ff si se usan
            return render_template('mejores_clientes.html', form = form, fc = True, consulta = consulta, msg2 = "Importe")
        return render_template('mejores_clientes.html', form = form)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

@app.route("/mas_vendidos", methods = ('GET', 'POST'))
def mas_vendidos():
    """En esta pagina se generara y visualizara el listado de los productos de mayor venta para realizar esto se
    necesita:
          l- a cantidad de productos que se quiere mostrar, el usuario ingresara este dato.
          2- la informacion de las ventas se obtiene del archivo archivo.csv, el cual sera leido y asignados los datos
           en la variable listado.
          3- la  variable lista_busqueda en la cual se asigna el listado de productos sin duplicados que contiene el
          archivo archivo.csv.
          Primero se genera una lista que contiene el nombre del producto, cantidad vendida y codigo, y luego con ella
          se genera otra lista con la cantidad de items que pide el usuario, se la ordena para que los valores sean
          visualizados en forma descendente."""
    if session.get("nombre"):
        form = MyConsulta()
        if form.validate_on_submit():
            listado = archivo.leer("archivos_csv/archivo.csv")
            masvendio = []
            consulta = []
            lista_busqueda = archivo.lista_producto("archivos_csv/archivo.csv")
            for listcli in lista_busqueda:
                cant = 0
                codigo = 0
                for clientes in listado:
                    if listcli == clientes['PRODUCTO']:
                         cant = cant + float(clientes['CANTIDAD'])
                         codigo = clientes['CODIGO']
                masvendio.append([int(cant), listcli, codigo])
            cont = 1
            masvendio.sort(reverse = True)
            for datos in masvendio:
                if cont <= form.cantidad.data:
                    consulta.append(datos)
                    cont = cont + 1
            consulta.sort(reverse = True)
            return render_template('mas_vendidos.html', form = form, fc = True, consulta = consulta, msg2 = "Cantidad")
        return render_template('mas_vendidos.html', form = form)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

@app.errorhandler(404)
def no_encontrado(e):
    """en caso de error se muestra la pagina 404.html"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    """en caso de error se muestra la pagina 500.html"""
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()
