from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,DateField, validators
from wtforms.validators import DataRequired, Email, Length

class Categories(FlaskForm):
    IdCategoria = StringField('Id categoría')
    NombreCategoria = StringField('Nombre de la categoría', validators=[
        DataRequired(
            message='El nombre de la categoría es obligatoria'
        ),
        Length(
            min=5,
            max=45,
            message='Mínimo 5 caratéres y máximo 45'
        )])