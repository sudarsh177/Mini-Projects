from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from typing import Callable
import requests
import os


api_key = os.getenv("api_key")
URLA = "https://api.themoviedb.org/3/search/movie"


app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'top secret'

class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique = True, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(100), nullable = False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(200))
    img_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Movie {self.title}>'


class UpdateForm(FlaskForm):
    rating = FloatField(label='Your Rating on 0-10 scale', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    name = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    db.session.commit()
    return render_template("index.html", movies = all_movies)


@app.route("/update", methods = ["GET","POST"])
def update():
    update_form = UpdateForm()
    movie_id = request.args.get('id')
    movie_info = Movie.query.get(movie_id)
    if update_form.validate_on_submit():
        movie_info.rating = update_form.rating.data
        movie_info.review = update_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movies = movie_info, form = update_form)


@app.route("/delete", methods = ["GET","POST"])
def delete():
    movie_id = request.args.get('id')
    movie_info = Movie.query.get(movie_id)
    db.session.delete(movie_info)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods = ["GET","POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_name = add_form.name.data
        parameters = {
            'api_key': api_key,
            'query': movie_name,
        }
        response = requests.get(url=URLA, params=parameters)
        data = response.json()["results"]
        return render_template('select.html', data = data)


    return render_template("add.html", form = add_form)


@app.route("/find", methods = ["GET","POST"])
def find():
    movie_api = request.args.get('id')
    new_url = f'https://api.themoviedb.org/3/movie/{movie_api}'
    response = requests.get(new_url, params={"api_key": api_key})
    data = response.json()

    new_movie = Movie(
        title=data['title'],
        year= data['release_date'].split('-')[0],
        description= data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500/{data['backdrop_path']}"
    )

    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('update',id = new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
