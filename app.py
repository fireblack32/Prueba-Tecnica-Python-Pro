from flask import Flask,render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
from config import config

from math import sq

#from flask_mysqldb import MySQL
app = Flask(__name__)
import json
import ast

conexion=MySQL(app)

# configuraciones 
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET'])
def Index():
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT id, circulacion, pago FROM tabla" #Nombre del campo o columna
        cursor.execute(sql) #sentencia o ejecutar consulta
        datos=cursor.fetchall()  #convierte la respuesta en algo entendible para python
        return render_template('index.html', contacts = datos)
    except Exception as ex:
        return  "Error"


@app.route('/', methods=['POST'])
def DataRegister():
    if request.method =='POST':  
        circulacion = request.form['circulacion']
        pago =request.form['pago']
        # print(circulacion)
        # print(pago)
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO tabla (circulacion, pago) 
        VALUES ('{0}', '{1}')""".format(circulacion, pago)
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de insercion
        flash('Dato Recibido Correctamente')
        return redirect(url_for('Index'))
    
#Editar tabla
@app.route('/editar/<id>', methods=['GET']) 
def editar_tabla(id):
        """Redireccion al editor del dato a travez de el id obtenido de la BD

        Args:
            id (string): clave principal de el elemento a editar

        Returns:
            contact: se retorna el id a esditar a la seccion de edción.
        """
        cursor=conexion.connection.cursor()
        sql = "SELECT id, circulacion, pago FROM tabla WHERE id = {0}".format(id) #Nombre del campo o columna
        cursor.execute(sql) #sentencia o ejecutar consulta
        datos=cursor.fetchall()  #convierte la respuesta en algo entendible para python
        return render_template('editar.html', contact = datos[0])

@app.route('/update/<id>', methods=['POST']) 
def actualizar_tabla(id):
    if request.method =='POST':  
        circulacion = request.form['circulacion']
        pago =request.form['pago']
        cursor=conexion.connection.cursor()
        sql = """UPDATE tabla SET circulacion = '{0}', pago = '{1}'
        WHERE id = '{2}'""".format(circulacion, pago, id)
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de insercion
        flash('Dato Actualizado Correctamente')
        return redirect(url_for('Index'))


#Eliminar dato de la tabla especifico       
@app.route('/delete/<string:id>') #con o sin el tipo de dato
def eliminar_tabla(id):
    """Definicion de la funcion para eliminar un dato en especifico

    Args:
        id (string ): clave principal de el elemento a editar

    Returns:
        Index: Despues de seleccionar el elemento a eliminar llamamos a la pagina pricipal para refrescar 
        la pagina y se muestre el dato eliminado
    """
    try: 
        cursor= conexion.connection.cursor()
        sql = "DELETE FROM tabla WHERE id = {0}".format(id)
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de insercion
        flash('Dato Eliminado Correctamente')
        return redirect(url_for('Index'))
    except Exception as ex:
        return "Error"
    
@app.route('/conteo', methods=['GET']) 
def conteo_tabla():
        """Muestra del registro total en la sección count.html

        Returns:
            counts: se envía las variables de lectura a la sección count.html para que se muestren los 
            resultados de entrada y metodos de pago total
        """
        cursor=conexion.connection.cursor()
        sql = "SELECT id, circulacion, pago FROM tabla" #Nombre del campo o columna
        cursor.execute(sql) #sentencia o ejecutar consulta
        datos=cursor.fetchall()  #convierte la respuesta en algo entendible para python
        print(type(datos))
        CountEntra = 0
        CountSale = 0
        CountEfectivo = 0
        CountTarjeta = 0
        CountTotal = 0
        
        for t in range(len(datos)):
                    
            if "Entra" in datos[t]:
                CountEntra += 1

            if "Sale" in datos[t]:
                CountSale += 1
            
            if "Efectivo" in datos[t]:
                CountEfectivo += 1            
            
            if "Tarjeta" in datos[t]:
                CountTarjeta += 1 
                
            CountTotal += 1 
            
            print(datos[t])
            print(CountEntra, CountSale, CountEfectivo, CountTarjeta, CountTotal)
        
        return render_template('count.html', CountEntra = CountEntra, CountSale = CountSale, CountEfectivo = CountEfectivo, CountTarjeta = CountTarjeta, CountTotal = CountTotal)
        
def pagina_no_encontrada(error):
    return "<h1>la pagina que intentas buscar no existe ...</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)