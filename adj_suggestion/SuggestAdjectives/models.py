from django.db import models


# Create your models here.
class Synonyms(models.Model):
    word = models.TextField('original', max_length=200)
    syn = models.TextField('syn', max_length=200)