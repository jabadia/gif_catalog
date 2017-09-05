import random
import re
from operator import and_

from django.db.models import Q

from backend.models import GifPicture


class GifPictureManager:
    all_words = None

    @classmethod
    def get_random_pics(cls, how_many=18):
        pics_count = GifPicture.objects.all().count()
        picked_ids = random.sample(range(pics_count), how_many)

        gif_pictures = GifPicture.objects.filter(id__in=picked_ids).order_by('-upload_date')
        return list(gif_pictures)

    @classmethod
    def search(cls, q, start=0, how_many=18):
        gif_pictures = GifPicture.objects.filter(
            reduce(and_, [Q(title__icontains=term) for term in q])
        ).order_by('-upload_date')[start:start+how_many]
        return list(gif_pictures)

    @classmethod
    def get_most_recent_pics(cls, how_many=18):
        gif_pictures = GifPicture.objects.all().order_by('-upload_date')[:how_many]
        return list(gif_pictures)

    @classmethod
    def get_search_suggestions(cls, q):

        # calculate all words, just once
        if cls.all_words is None:
            all_pics = GifPicture.objects.all()
            cls.all_words = set(word.lower() for pic in all_pics for word in re.findall(r"[\w']+", pic.title))

        q = q.lower()
        return sorted(
            {word for word in cls.all_words if q in word},               # find matching words
            key=lambda word: '_' + word if word.startswith(q) else word  # sort first words that start with q
        )
