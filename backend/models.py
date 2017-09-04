# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class GifPicture(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    gifurl = models.URLField()
    upload_date = models.DateTimeField(auto_now_add=True)
