from flask import Blueprint, render_template, flash, redirect, url_for
from werkzeug.security import check_password_hash

from source import User
from source.auth_app.auth_forms import LoginForm, RegistrationForm
from source.extensions import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', category='info')
        return redirect(url_for('to_do.index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user, remember=True)
                return redirect(url_for('to_do.list_todos'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist', category='error')
    return render_template('auth/login.html', form=form, user=current_user)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        phone_number = form.phone_number.data
        new_user = User(email=email, phone_number=phone_number)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration was successfull, please login")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out successfully!")
    return redirect(url_for('auth.login'))