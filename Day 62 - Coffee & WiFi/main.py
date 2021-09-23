from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    loc = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    optime = StringField('Opening Time e.g. 8:00 AM', validators=[DataRequired()])
    cltime = StringField('Closing Time e.g. 5:00 PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating',
                         choices=[('✘', '✘'), ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
                         validators=[DataRequired()])
    power = SelectField('Power Socket Availability',
                        choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                                 ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')],
                        validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating',
                       choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
                       validators=[DataRequired()])    
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", 'a', encoding="utf8") as f1:
            f1.write("\n")
            f1.write(form.data['cafe'] + ",")
            f1.write(form.data['loc'] + ",")
            f1.write(form.data['optime'] + ",")
            f1.write(form.data['cltime'] + ",")
            f1.write(form.data['coffee'] + ",")
            f1.write(form.data['wifi'] + ",")
            f1.write(form.data['power'])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
