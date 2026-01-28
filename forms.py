from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, EmailField, validators

class UserForm(Form):
    matricula=IntegerField("Matricula", {
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    })
    nombre=StringField("Nombre", {
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
    })
    apellidoP=StringField("Apeliido Paterno", {
        validators.DataRequired(message="El campo es requerido"),

    })
    apellidoM=StringField("Apeliido Materno", {
        validators.DataRequired(message="El campo es requerido"),

    })
    correo=EmailField("Correo", {
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingresa correo valido")
        
    })