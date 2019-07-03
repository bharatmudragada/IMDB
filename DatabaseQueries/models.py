from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import F, Count, Q
import random

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class MovieCast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    cast = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    actors = models.ManyToManyField(MovieCast, related_name="movie_actors")


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating_no = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    no_of_ratings = models.IntegerField()

    def __str__(self):
        return str(self.movie_id) + " " + str(self.avg_rating)


def get_rating_data():
    id = 1
    ratings = []
    for i in range(1, 12):
        for j in range(1,6):
            ratings.append({"id": id, "movie_id": i, "rating_no": j, "no_of_ratings": random.randint(1, 15)})
            id += 1
    return ratings


def populateDb():
    Actor.objects.all().delete()
    actors = [{"id": 1, "name": "Pavan Kalyan", "gender": "M", "birth_date": "1987-09-01"},
              {"id": 2, "name": "Prabhas", "gender": "M", "birth_date": "1998-02-12"},
              {"id": 3, "name": "Ram Charan", "gender": "M", "birth_date": "1999-09-03"},
              {"id": 4, "name": "NTR", "gender": "M", "birth_date": "1998-09-21"},
              {"id": 5, "name": "Nani", "gender": "M", "birth_date": "1992-07-22"},
              {"id": 6, "name": "Nithin", "gender": "M", "birth_date": "1991-01-01"},
              {"id": 7, "name": "Bala Krishna", "gender": "M", "birth_date": "1981-03-15"},
              {"id": 8, "name": "Samantha", "gender": "F", "birth_date": "1997-04-01"},
              {"id": 9, "name": "Tamanna", "gender": "F", "birth_date": "1998-04-21"},
              {"id": 10, "name": "Anushka", "gender": "F", "birth_date": "1999-11-12"},
              {"id": 11, "name": "Rashi", "gender": "F", "birth_date": "1999-10-11"},
              {"id": 12, "name": "Deepika", "gender": "F", "birth_date": "1997-09-12"},
              {"id": 13, "name": "Katrina", "gender": "F", "birth_date": "1999-09-22"}
              ]
    Actor.objects.bulk_create([Actor(**vals) for vals in actors])

    Movie.objects.all().delete()
    movies = [{"id": 1, "title": "A", "release_date": "2012-02-03"},
             {"id": 2, "title": "B", "release_date": "2014-03-01"},
             {"id": 3, "title": "C", "release_date": "2013-05-13"},
             {"id": 4, "title": "D", "release_date": "2013-01-06"},
             {"id": 5, "title": "E", "release_date": "2014-03-15"},
             {"id": 6, "title": "F", "release_date": "2015-12-09"},
             {"id": 7, "title": "G", "release_date": "2012-09-03"},
             {"id": 8, "title": "H", "release_date": "2012-12-21"},
             {"id": 9, "title": "I", "release_date": "2012-01-21"},
             {"id": 10, "title": "J", "release_date": "2012-12-16"},
             {"id": 11, "title": "K", "release_date": "2013-02-12"},
             ]
    Movie.objects.bulk_create([Movie(**vals) for vals in movies])

    MovieCast.objects.all().delete()
    moviecasts = [{"id": 1, "movie_id": 1, "cast_id": 1, "role": "Hero"},
                  {"id": 2, "movie_id": 1, "cast_id": 8, "role": "Heroine"},
                  {"id": 3, "movie_id": 1, "cast_id": 9, "role": "Heroine"},
                  {"id": 4, "movie_id": 2, "cast_id": 2, "role": "Hero"},
                  {"id": 5, "movie_id": 2, "cast_id": 10, "role": "Heroine"},
                  {"id": 6, "movie_id": 3, "cast_id": 3, "role": "Hero"},
                  {"id": 7, "movie_id": 3, "cast_id": 11, "role": "Heroine"},
                  {"id": 8, "movie_id": 4, "cast_id": 4, "role": "Hero"},
                  {"id": 9, "movie_id": 4, "cast_id": 12, "role": "Heroine"},
                  {"id": 10, "movie_id": 5, "cast_id": 1, "role": "Hero"},
                  {"id": 11, "movie_id": 5, "cast_id": 13, "role": "Heroine"},
                  {"id": 12, "movie_id": 6, "cast_id": 5, "role": "Hero"},
                  {"id": 13, "movie_id": 6, "cast_id": 10, "role": "Heroine"},
                  {"id": 14, "movie_id": 7, "cast_id": 1, "role": "Hero"},
                  {"id": 15, "movie_id": 7, "cast_id": 11, "role": "Heroine"},
                  {"id": 16, "movie_id": 8, "cast_id": 3, "role": "Hero"},
                  {"id": 17, "movie_id": 8, "cast_id": 12, "role": "Heroine"},
                  {"id": 18, "movie_id": 9, "cast_id": 5, "role": "Hero"},
                  {"id": 19, "movie_id": 9, "cast_id": 13, "role": "Heroine"},
                  {"id": 20, "movie_id": 10, "cast_id": 2, "role": "Hero"},
                  {"id": 21, "movie_id": 10, "cast_id": 11, "role": "Heroine"},
                  {"id": 22, "movie_id": 11, "cast_id": 4, "role": "Hero"},
                  {"id": 23, "movie_id": 11, "cast_id": 12, "role": "Heroine"},
                  ]
    MovieCast.objects.bulk_create([MovieCast(**vals) for vals in moviecasts])


    MovieRating.objects.all().delete()
    movierating = get_rating_data()
    MovieRating.objects.bulk_create([MovieRating(**vals) for vals in movierating])


def get_top_10_movies_with_avg_rating():
    rating_1_value = Q(rating_no=1).count()
    top_10_movies = MovieRating.objects.all().annotate(avg_rating=rating_1_value).order_by('-avg_rating')[:10]
    return top_10_movies


def get_top_5_and_least_5_actors():
    no_of_movies_acted = Actor.objects.annotate(no_of_movies_acted=Count('moviecast')).values_list('name', 'no_of_movies_acted')
    top_5_actors = no_of_movies_acted.order_by('-no_of_movies_acted')[:5]
    least_5_actors = no_of_movies_acted.order_by('no_of_movies_acted')[:5]
    result = {"top": top_5_actors, "least": least_5_actors}
    return result

#
# def get_5_yongest_and_oldest_movies():
#     movie_avg_age =