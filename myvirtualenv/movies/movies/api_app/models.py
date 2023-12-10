from django.db import models

# Create your models here.

class Actors(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    actor_first_name = models.CharField(max_length=100)
    actor_last_name = models.CharField(max_length=100)
    actor_species = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.actor_id=}, {self.actor_first_name=}, {self.actor_last_name=}, {self.actor_species=}"

class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_language = models.CharField(max_length=100)
    movie_release_country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.movie_id=}, {self.movie_name=}, {self.movie_language}, {self.movie_release_country}"

class MovieCast(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    actor_id = models.ForeignKey(Actors, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    class Meta:
        unique_together = (("movie_id", "actor_id"),)

    def __str__(self):
        return f"{self.movie_id=}, {self.actor_id=}, {self.role=}" + "\n"*5