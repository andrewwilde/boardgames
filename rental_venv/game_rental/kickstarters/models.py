# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4
from django.db import models


class KickStarter(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4)
    slug=models.CharField(max_length=200)
    kickstarter_id=models.CharField(unique=True, max_length=50)
    category_id=models.CharField(max_length=5)

    @property
    def iframe(self):
        return "https://www.kickstarter.com/projects/%s/%s/widget/card.html?v=2" % (self.kickstarter_id, self.slug)
