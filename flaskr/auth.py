import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' :
        login = request.form['name']
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None

        flash("Values from form: login={login}, email={email}, password={password}")

        if not login:
            error = 'Login is required!\n'
        elif not password:
            error = 'Password is required!\n'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (login, email, password) VALUES (?,?,?)",
                    (login, email, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {login} is already exists!"
            else:
                return redirect(url_for('auth.login'))
            
        flash(error)
    
    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'] 
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?',
            (email,)
        ).fetchone()

        if user is None:
            error = "No user with email '{email}'!\n"
        elif not check_password_hash(user[password], password):
            error = 'Wrong password!\n'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?',
            (user_id,)
        ).fetchone()

@bp.route('logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view