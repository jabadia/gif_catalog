from django.forms import model_to_dict
from django.http import JsonResponse

from gif_picture_manager import GifPictureManager


def api_login_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'msg': 'unauthorized'}, status=403)
    return _wrapped_view_func


@api_login_required
def pics(request):
    how_many = 18
    gif_pictures = [model_to_dict(pic) for pic in GifPictureManager.get_random_pics(how_many)]

    result = {
        'pics': gif_pictures,
    }
    return JsonResponse(result)
