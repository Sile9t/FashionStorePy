from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Установите секретный ключ для сессий и flash-сообщений

# Пример "базы данных" пользователей
users = {
    "admin@example.com": {
        "name": "Admin",
        "password_hash": generate_password_hash("password")
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('pass')
        
        user = users.get(email)
        if user and check_password_hash(user['password_hash'], password):
            session['user_email'] = email
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Неверный логин или пароль', 'error')
    return render_template('sign_in.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        password = request.form.get('pass')
        
        if email in users:
            flash('Пользователь с таким email уже существует', 'error')
        else:
            users[email] = {
                "name": name,
                "password_hash": generate_password_hash(password)
            }
            flash('Регистрация прошла успешно! Пожалуйста, войдите.', 'success')
            return redirect(url_for('sign_in'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        flash('Пожалуйста, войдите в систему', 'error')
        return redirect(url_for('sign_in'))
    return "Добро пожаловать в личный кабинет!"

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('index'))

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        return 'Product is posted'
    return render_template('prodList.html')

if __name__ == '__main__':
    app.run(debug=True)