# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import OwnedGame, BorrowedGame, BoardGame

# Register your models here.
admin.site.register(BoardGame)
admin.site.register(OwnedGame)
admin.site.register(BorrowedGame)
