
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import CrimeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/crimes.db'
db = SQLAlchemy(app)

class CrimeRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    crime = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)

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

if __name__ == "__main__":
    app.run(debug=True)
  