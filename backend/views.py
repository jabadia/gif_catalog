# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from gif_picture_manager import GifPictureManager


def index(request):
    how_many = 18
    gif_pictures = GifPictureManager.get_random_pics(how_many)

    context = {
        'msg': "randomly picked images",
        'gif_pictures': gif_pictures,
    }
    return render(request, 'index.html', context)
