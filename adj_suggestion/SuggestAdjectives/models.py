from django.db import models


# Create your models here.
class Synonym(models.Model):
    word = models.TextField('original', max_length=200)
    syn = models.TextField('syn', max_length=200)
    # reported = models.IntegerField('report count')


class Adjective(models.Model):
    word = models.TextField('word', max_length=200)
    synonyms = models.ManyToManyField('self')
    is_ready = models.BooleanField('is crawled?', default=False)
