from django.db import models
from django.core.validators import int_list_validator, RegexValidator


class Movie(models.Model):

    poster_path=models.CharField(max_length=35,null=True)
    adult=models.BooleanField()
    overview=models.TextField()
    release_date=models.CharField(max_length=12)

    genre_ids = models.TextField(validators=[int_list_validator]) 
        #ArrayField(ArrayField(models.IntegerField())) is only comapatible with postgresql, can be used instead 
    
    tmdb_id=models.IntegerField()
    original_title=models.TextField()
    original_language=models.CharField(max_length=10)
    title=models.TextField()
    backdrop_path=models.CharField(max_length=35,null=True)
    popularity=models.FloatField()
    vote_count=models.IntegerField()
    video=models.BooleanField()
    vote_average=models.FloatField()
    tags=models.TextField(null=True)

    def __str__(self):
        return self.title

# many-to-many data model 
class MovieList(models.Model):

    codename = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed')]
        )

    movies= models.ManyToManyField('Movie',related_name='movies')
    listtags=models.TextField(null=True)
    recommended=models.ManyToManyField('Movie',related_name='recommended')
    
    def __str__(self):
        return self.codename
 

