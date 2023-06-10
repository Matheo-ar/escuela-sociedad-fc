from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,DateField, validators
from wtforms.validators import DataRequired, Email, Length

class Campus(FlaskForm):
    NombreSede = StringField('Nombre Sede', [
                            validators.DataRequired(message='El nombre de la sede es obligatorio'),
                            validators.Length(
                            min=10,
                            max=60,
                            message='Minimo 10 caracteres máximo 60')])
    Direccion = StringField('Direccion', validators=[
                            DataRequired(
                            message='La dirección es obligatoria'),
                            Length(
                            max=60
                            )])
    Telefono = StringField('Teléfono', validators=[
                            DataRequired(
                            message='El teléfono es obligatorio'
                            ),
                            Length(
                            max=10,
                            message='Debe ser de máximo 10 digitos'
                           )])
    Director = StringField('Director', [
                            validators.DataRequired(
                            message='El director es obligatorio'),
                            validators.Length(
                            min=3,
                            max=60,
                            message='Minimo 3 caracteres máximo 60'),
                            ])
    ActiveCampus = StringField('Estado: ', validators=[
                            DataRequired(
                            message='El estado es obligatorio'
                            )])
    Submit = SubmitField('Registrar')
