# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    context = {
        'msg': "randomly picked images",
        'user': request.user,
    }
    return render(request, 'index.html', context)
