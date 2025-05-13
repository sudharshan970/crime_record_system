from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import CrimeForm
import secrets

app = Flask(_name_)
app.config['SECRET_KEY'] = 'this_should_be_secret_and_random' 
app.config['SECRET_KEY'] = 'e3f9bcfc4a2e49e4b77a9dd71d9c4c4f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crime_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class CrimeRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    crime = db.Column(db.String(100))
    date = db.Column(db.String(50))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_crime():
    form = CrimeForm()
    if form.validate_on_submit():
        crime = CrimeRecord(
            name=form.name.data,
            crime=form.crime.data,
            date=form.date.data
        )
        db.session.add(crime)
        db.session.commit()
        return redirect(url_for('view_crimes'))
    return render_template('add_crime.html', form=form)

@app.route('/crimes')
def view_crimes():
    crimes = CrimeRecord.query.all()
    return render_template('view_crimes.html', crimes=crimes)

if _name_ == "_main_":
    app.run(debug=True)
if _name_ == "_main_":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
