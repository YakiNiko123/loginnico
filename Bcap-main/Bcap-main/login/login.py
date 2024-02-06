import hashlib
import mysql.connector
from flask import Flask, request, redirect, session, render_template


programa = Flask(__name__)
programa.secret_key = 'nicolasvanegas'
"mysql = MySQL()"
conexion = mysql.connector.connect(user='root', password='', host='localhost', database='bcap')


cursor = conexion.cursor()



@programa.route('/')
def index():
    return render_template('login.html')

@programa.route('/recuperar')
def boton_recuperar():
    return render_template('recuperar.html')


@programa.route('/login', methods = ['GET','POST'])
def login():
    if request.method =='POST':
        correo = request.form['correo_enviado']
        contrasena = request.form['contrasena']
        hashed_contrasena= hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
        consulta = f"SELECT correo_electronico,contrasena FROM instructor WHERE correo_electronico='{correo}' AND contrasena='{hashed_contrasena}'"
        
        
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        conexion.commit()

        print(resultado)
        print(hashed_contrasena)
        

        if (resultado):
            if hashed_contrasena == resultado[0][1]:
                session['logueado'] = True
                return render_template('recuperar.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html', error = 'Usuario o contraseña incorrectos')
        
        

if __name__ == '__main__':
    programa.run(host='0.0.0.0', debug=True,port=8080)





