import random
from backend.models import GifPicture


class GifPictureManager:
    @classmethod
    def get_random_pics(cls, how_many=18):
        pics_count = GifPicture.objects.all().count()
        picked_ids = random.sample(range(pics_count), how_many)

        gif_pictures = GifPicture.objects.filter(id__in=picked_ids).order_by('-upload_date')
        return list(gif_pictures)

    @classmethod
    def get_most_recent_pics(cls, how_many=18):
        gif_pictures = GifPicture.objects.all().order_by('-upload_date')[:how_many]
        return list(gif_pictures)

