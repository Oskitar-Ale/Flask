from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user,login_required
from flask_wtf.csrf import CSRFProtect
from config import config



# Models
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User




app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0,request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required

def protected():
    return "<h1>Seccion para usuarios autenticados</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()


















#Comprobacion de conexion con la db
# from flask import Flask
# from flask_mysqldb import MySQL
# from config import config

# app = Flask(__name__)

# db = MySQL(app)

# @app.route('/')
# def index():
#     cur = db.connection.cursor()
#     cur.execute('SELECT 1')
#     result = cur.fetchone()
#     cur.close()
#     return 'Connection successful'

# if __name__ == '__main__':
#     app.config.from_object(config['development'])
#     try:
#         app.run()
#     except Exception as e:
#         print(f'Error: {e}')
