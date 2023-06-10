from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,DateField, validators
from wtforms.validators import DataRequired, Email, Length


class Attendant(FlaskForm):
    Tipodoc = StringField('Tipo Documento', validators=[
        DataRequired(
            message='El tipo de documento es obligatorio'
        )])
    Documento = StringField('Número Documento', [
                            validators.DataRequired(
                                message='El documento es obligatorio'),
                            validators.Length(
                                min=3,
                                max=20,
                                message='Minimo 3 caracteres máxinmo 20'),
                            validators.Regexp(
                                '^[0-9]+$',
                                message='Solo se aceptan números'
                            )])
    Nombres = StringField('Nombres', [
        validators.DataRequired(message='El nombre es obligatorio'),
        validators.Length(
            min=3,
            max=60,
            message='Minimo 3 caracteres máxinmo 60'),
       ])
    Apellidos = StringField('Apellidos', [
                            validators.DataRequired(
                                message='El apellido es obligatorio'),
                            validators.Length(
                                min=3,
                                max=60,
                                message='Minimo 3 caracteres máxinmo 60'),
                           ])
    Nacimiento = DateField('Fecha de Nacimiento', [
        validators.DataRequired(
            message='La fecha de nacimiento es obligatoria'
        )])
    Genero = StringField('Genero', validators=[
        DataRequired(
            message='El genero es obligatorio'
        )])
    Email = StringField('Correo electronico', validators=[
                        DataRequired(
                            message='El correo electrónico es obligatorio'),
                        Email(
                            message='Debe ser de tipo correo electrónico'
                        )])
    Telefono = StringField('Teléfono', validators=[
                           DataRequired(
                               message='El teléfono es obligatorio'
                           ),
                           Length(
                               max=10,
                               message='Debe ser de máximo 10 digitos'
                           )])
    Direccion = StringField('Direccion', validators=[
                            DataRequired(
                                message='La dirección es obligatoria'),
                            Length(
                                max=60
                            )])
    Contrasena = PasswordField('Contraseña', [
                               validators.DataRequired(
                                   message='La contraseña es obligatoria'),
                               validators.Length(
                                   min=8,
                                   max=60,
                                   message='La contraseña debe ser minimo de 8 caractéres'),
                               validators.Regexp(
                                   regex='^(?=.*[A-Z])(?=.*[0-9]).*$',
                                   message='La contraseña debe contener al menos una mayúscula y un número'
                               )])
    Submit = SubmitField('Registrar')