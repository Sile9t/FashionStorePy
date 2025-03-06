from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('pass')
      
        if email == "admin@example.com" and password == "password":  
            return redirect(url_for('dashboard'))
        return "Неверный логин или пароль"
    return render_template('sign_in.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        password = request.form.get('pass')
  
        return redirect(url_for('sign_in'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    return "Добро пожаловать в личный кабинет!"


if __name__ == '__main__':
    app.run(debug=True)
