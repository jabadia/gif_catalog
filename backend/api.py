from django.forms import model_to_dict
from django.http import JsonResponse

from gif_picture_manager import GifPictureManager


def pics(request):
    how_many = 18
    gif_pictures = [model_to_dict(pic) for pic in GifPictureManager.get_random_pics(how_many)]

    result = {
        'pics': gif_pictures,
    }
    return JsonResponse(result)
