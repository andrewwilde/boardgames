# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

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


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class OwnedGame(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    game=models.ForeignKey(BoardGame, on_delete=models.CASCADE)


class BorrowedGame(models.Model):
    ownedgame=models.ForeignKey(OwnedGame, models.Model)
    borrower=models.ForeignKey(User, on_delete=models.CASCADE)


