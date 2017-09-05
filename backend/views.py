# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render

from backend.models import GifPicture


def index(request):
    count = GifPicture.objects.all().count()
    all_ids = range(count)
    random.shuffle(all_ids)
    picked_ids = all_ids[:18]

    # gif_pictures = GifPicture.objects.all().order_by('-upload_date')[:18]
    gif_pictures = GifPicture.objects.filter(id__in=picked_ids).order_by('-upload_date')

    context = {
        'msg': "randomly picked images",
        'gif_pictures': gif_pictures,
    }
    return render(request, 'index.html', context)
