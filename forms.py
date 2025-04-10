
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CrimeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    crime = StringField('Crime', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Record')
