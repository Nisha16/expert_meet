from app import app
from app import db
from flask import render_template, flash, redirect, url_for
from app.forms import UserForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['GET', 'POST'])
def user_data():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, interest=form.interest.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for submitting the details {}'.format( form.username.data))
        return redirect(url_for('index'))
    return render_template('user_form.html', title='Schedule', form=form)