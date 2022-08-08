from wtforms import Form, validators, PasswordField, EmailField, StringField, StringField, TextAreaField
from werkzeug.datastructures import MultiDict

class FlaskForm(Form):

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        formdata = MultiDict(formdata)
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)

class LoginForm(FlaskForm):
    email = EmailField("email", validators=[
        validators.InputRequired()
    ])
    password = PasswordField("password", validators=[
        validators.InputRequired()
    ])

class SignUpForm(LoginForm):
    confirm = PasswordField("comfim", validators=[
        validators.InputRequired(),
        validators.EqualTo('password')
    ])
    username = StringField("username", validators=[validators.InputRequired()])

class WorkspaceForm(FlaskForm):
    name = StringField("email", validators=[validators.InputRequired()])
    description = TextAreaField("description", validators=[validators.InputRequired()])