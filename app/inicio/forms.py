from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField,DecimalField
from wtforms.validators import DataRequired, Email, Length


class Login(FlaskForm):
    Documento = StringField('No. Documento', validators=[
                            DataRequired(
                                message='El número de documento es obligatorio'
                            )])
    Contrasena = PasswordField('Contraseña', validators=[
                               DataRequired(
                                   message='La contraseña es obligatoria'
                               )])
    Submit = SubmitField('Ingresar')
