from django.db import models
class Person(models.Model):
    ROLE_CHOICES = [
        ('ACTOR', 'Actor'),
        ('DIRECTOR', 'Director'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    movies = models.ManyToManyField('Movie', related_name='people')

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    rating = models.IntegerField()
    description = models.TextField()
    director = models.ForeignKey(Person,on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='genre')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    comment = models.TextField()
    review_date = models.DateField(auto_now_add=True)
