from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
from pprint import pprint
from dotenv import dotenv_values

config = dotenv_values(".env")


TMDB_API_KEY = config['TMDB_API_KEY']

app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float(), nullable=True)
    ranking = db.Column(db.Integer(), nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        movie_id_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
        data = requests.get(f"{movie_id_url}").json()['results'][:5]
        movie_data = []
        for movie in data:
            pprint(movie)
            new_movie = {
                'id': movie['id'],
                'title': movie['title'],
                'year': movie['release_date'].split('-')[0]
            }
            movie_data.append(new_movie)
        pprint(movie_data)
        return render_template('select.html', movie_data=movie_data)
    else:
        return render_template('add.html', form=form)


@app.route('/addnew/<int:movid>')
def addnew(movid):
    image_url = "http://image.tmdb.org/t/p/w500"
    movie_data_url = f"https://api.themoviedb.org/3/movie/{movid}"
    mov_dat_params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }
    response = requests.get(movie_data_url, params=mov_dat_params).json()
    new_movie = Movie(
        id=movid,
        title=response['original_title'],
        description=response['overview'],
        year=response['release_date'].split('-')[0],
        img_url=f"{image_url}{response['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('update', movid=movid))


@app.route('/update/<int:movid>', methods=['GET', 'POST'])
def update(movid):
    form = RateMovieForm()
    if form.validate_on_submit():
        upd_mov = Movie.query.get(movid)
        review = form.review.data
        rating = form.rating.data
        upd_mov.review = review
        upd_mov.rating = rating
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', form=form)


@app.route('/delete/<int:movid>')
def delete(movid):
    movie = Movie.query.get(movid)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
