from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequiered, Email, Length

class SinginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequiered(), Email() ])
    password = PasswordField('Password', validators=[DataRequiered()])
    submit = SubmitField('Entrar')