from flask import Flask, render_template, redirect, flash, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class OverrideRequestForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    reason = TextAreaField('Reason for Override', validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[DataRequired()])
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
        # Process the form data and perform necessary actions, e.g., storing data in a database.
        # You can also send an email notification to the relevant department.
        flash('The course override request has been submitted!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
