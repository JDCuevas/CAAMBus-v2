from wtforms import Form, StringField, TextAreaField, PasswordField, SelectField, validators
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField

def validate_license(form, field):
	data_len = len(field.data)
	if (data_len > 0 and data_len < 7) or (data_len > 7):
		raise ValidationError('License must be empty or 7 characters long.')

class RegisterForm(Form):
	first_name = StringField('First Name', [validators.Length(min=1, max=30)])
	last_name = StringField('Last Name', [validators.Length(min=1, max=30)])
	phone = StringField('Phone', [validators.Length(min=12, max=12)])
	username = StringField('Username', [validators.Length(min=4, max=30)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match!')
		])
	confirm = PasswordField('Confirm Password')
	user_type = SelectField(u'User Type', choices=[('False', 'Driver'), ('True', 'Admin')])
	license = StringField('License', [validate_license])

class LoginForm(Form):
	username = StringField('Username', [validators.DataRequired()])
	password = PasswordField('Password', [validators.DataRequired()])

class ItineraryForm(Form):
	date = DateField('Date', format='%Y-%m-%d')
	start_time = TimeField('Start Time')
	end_time = TimeField('End Time')
	driver_id = SelectField(u'Driver', choices=[])
	trolley_id = SelectField(u'Trolley', choices=[])
	route_id = SelectField(u'Route', choices=[])