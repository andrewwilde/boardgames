# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4
from django.db import models

class BoardGame(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4)
    name=models.CharField(max_length=200)
    year_published=models.CharField(max_length=10)
    min_players=models.IntegerField()
    max_players=models.IntegerField()
    description=models.TextField()
    geek_rating=models.FloatField()
    average_rating=models.FloatField()
    ranking=models.IntegerField()

    #This needs to be added as a JSON field, but requires postgres
    #publisher=models.CharField(max_length=200)

    class Meta:
        unique_together = (("name", "year_published"))
