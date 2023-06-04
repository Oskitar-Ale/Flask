from flask import Flask
from flask import render_template





app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return 'Welcome'

@app.route('/register')
def registro():
    return 'Welcome'




if __name__ == '__main__':
    app.run()











