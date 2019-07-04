from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import F, Count, Q
import random
from django.db.models import Subquery, OuterRef, Sum, FloatField, Max, Count, IntegerField, Min, Avg
from django.db.models.functions import Cast
from django.db.models.functions import ExtractMonth
from django.db.models import F, ExpressionWrapper, fields

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, through="MovieCast")


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cast = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)


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
        return str(self.movie_id)


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
    movies = [{"id": 1, "title": "A", "release_date": "2012-04-03"},
             {"id": 2, "title": "B", "release_date": "2014-03-01"},
             {"id": 3, "title": "C", "release_date": "2013-05-13"},
             {"id": 4, "title": "D", "release_date": "2013-09-06"},
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
    top_10_movies = MovieRating.objects.values('movie_id', 'movie__title').annotate(avg_rating=Cast(Sum(F('no_of_ratings') * F('rating_no') * 1.0) / Sum(F('no_of_ratings')), FloatField()))
    return top_10_movies.values('movie__title','avg_rating').order_by('-avg_rating')[:10]


def get_top_5_and_least_5_actors():
    top_5_actors = Actor.objects.all().annotate(no_of_movies_acted=Count('moviecast')).order_by('-no_of_movies_acted').values('id')[:5]
    least_5_actors = Actor.objects.all().annotate(no_of_movies_acted=Count('moviecast')).order_by('no_of_movies_acted').values('id')[:5]
    no_of_movies_acted = Actor.objects.filter(Q(id__in=Subquery(top_5_actors)) | Q(id__in=Subquery(least_5_actors))).values_list('name')
    return no_of_movies_acted


def star_movies():
    star_month = MovieCast.objects.filter(movie_id=OuterRef('movie_id')).values('cast__birth_date__month').annotate(month_count=Count("id")).values_list('cast__birth_date__month', flat=True).order_by('-month_count', 'cast__birth_date__month')
    return MovieCast.objects.values('movie_id','cast__birth_date__month').annotate(month_count=Count("id"), star_month=Subquery(star_month[:1])).filter(movie__release_date__month=F('star_month'), cast__birth_date__month=F('star_month')).order_by('-month_count').values("movie_id","month_count")


def get_actors_movie_count_released_in_their_birth_month():
    return MovieCast.objects.annotate(release_month=ExtractMonth('movie__release_date'), birth_month=ExtractMonth('cast__birth_date')).filter(release_month=F('birth_month')).values("cast__name").annotate(movie_count=Count("movie"))


def difference_between_1star_and_5star():
    movie_difference = MovieRating.objects.filter(movie_id=OuterRef('movie_id')).values('movie_id').annotate(one_star=Sum('no_of_ratings', filter=Q(rating_no=1)), five_star=Sum('no_of_ratings', filter=Q(rating_no=5)), difference=F('one_star') - F('five_star')).values("difference")
    return MovieCast.objects.values("movie_id").annotate(difference=Subquery(movie_difference)).values("cast_id").annotate(difference_sum=Sum('difference')).order_by("-difference_sum")


def youngest_cast_age():
    age = ExpressionWrapper(F('movie__release_date') - F('cast__birth_date'), output_field=fields.DurationField())
    youngest_age = MovieCast.objects.filter(movie_id=OuterRef('id')).values('movie_id').annotate(age=age).order_by("age").values("age")[:1]
    return Movie.objects.annotate(youngest_age=Subquery(youngest_age)).values("id","youngest_age").order_by('youngest_age')[:10]


def year_in_which_most_cast_movies_released():
    return MovieCast.objects.values('movie__release_date__year').annotate(year_count=Count('movie__release_date__year')).order_by('-year_count')[:1]


def best_twin_stars():
    return MovieCast.objects.filter(movie__moviecast__movie__id=F('movie_id')).annotate(cast_to_id=F('movie__moviecast__cast__id')).filter(cast_id__lt=F('cast_to_id')).values("cast_id","cast_to_id").annotate(twin_count=Count("id")).order_by("-twin_count")[:1]


def youngest_and_oldest_movies_by_average_age_of_cast():
    age = ExpressionWrapper(F('movie__release_date') - F('cast__birth_date'), output_field=fields.DurationField())
    movie_avg_age = MovieCast.objects.values('movie_id').annotate(average_age=Avg(age))
    youngest_movies = movie_avg_age.order_by('average_age').values('movie_id')[:5]
    oldest_movies = movie_avg_age.order_by('-average_age').values('movie_id')[:5]
    return MovieCast.objects.filter(Q(movie_id__in=(Subquery(youngest_movies))) | Q(movie_id__in=(Subquery(oldest_movies)))).values("movie__title").distinct()
