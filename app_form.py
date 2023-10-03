from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard_to_guess_string'

bootstrap = Bootstrap(app)

class CourseOverrideForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    course_code = StringField('Course Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CourseOverrideForm()
    if form.validate_on_submit():
        student_name = form.student_name.data
        course_code = form.course_code.data
        flash('Course override request submitted successfully!', 'success')
        # You can process the request or store the data as needed here
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

