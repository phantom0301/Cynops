from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class NameForm(Form):
    name = StringField()
    submit = SubmitField('Submit')

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered.')

class IPscannerForm(Form):
    ip = StringField('IP address: ', validators=[DataRequired(), Length(1,17),Regexp('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}', 0, 'Must input right IP CIDR address')])
    submit = SubmitField('Scan')