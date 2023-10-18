"""
Author: Bryan Lizama Montecino 
Date: October 17, 2023

Assignment #3: Flask Web Application with Templates

Purpose:
To create an application where students can submit an override request. 
When the form is submitted, assuming all the necessary fields are entered, the application should show output to the user verifying the submission
"""

from flask import Flask, render_template, redirect, flash, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Regexp
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kachow_thor'

bootstrap = Bootstrap(app)
moment = Moment(app)

class OverrideRequestForm(FlaskForm):
    student_name = StringField('Enter your Full Name', validators=[DataRequired()])
    student_id = StringField('Enter your V-Number (Please enter the leading V and all 8 digits)', validators=[
        DataRequired(),
        Regexp('^V\d{8}$', message='V-Number must start with a "V" followed by 8 digits')
    ])
    student_email = StringField('Enter your VCU Email Address', validators=[DataRequired()])
    course_name = StringField('Course Name', validators=[DataRequired()])
    course_number = StringField('Enter the Course Number (For example: STAT 210)', validators=[DataRequired()])
    reason = TextAreaField('Reason for Override')
    submit = SubmitField('Submit Request')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = OverrideRequestForm()
    if form.validate_on_submit():
        # Process the form data
        flash('The course override request has been submitted!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8000)