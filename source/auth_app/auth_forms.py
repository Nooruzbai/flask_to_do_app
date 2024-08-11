from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, EmailField, validators,
                     PasswordField, DateTimeField, SubmitField)
from wtforms.validators import Length, EqualTo, DataRequired, Email


class RegistrationForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), validators.Email()])
    password = PasswordField(validators=[validators.Length(min=2, message='Too short')])
    password_confirm = PasswordField(validators=[EqualTo('password', 'Password mismatch')])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=5, max=30)])
    created_at = DateTimeField("Created_at", format="%Y-%m-%dT%H:%M:%S",
                               default=datetime.today,
                               validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
