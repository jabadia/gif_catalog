# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {
        'msg': "hi world!, I'm Django",
    }
    return render(request, 'index.html', context)
