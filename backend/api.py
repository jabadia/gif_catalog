from django.http import JsonResponse

from gif_picture_manager import GifPictureManager


def api_login_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'msg': 'unauthorized'}, status=403)
    return _wrapped_view_func


def _serialize_model(model, fields=None, exclude_fields=None, add_properties=None):
    exclude_fields = exclude_fields or []
    the_dict = {
        field.name: field.value_from_object(model)
        for field in model._meta.fields
        if (fields is None or field.name in fields) and field.name not in exclude_fields
    }
    if add_properties:
        for p in add_properties:
            the_dict[p] = getattr(model, p)
    return the_dict


@api_login_required
def pics(request):
    how_many = 18
    gif_pictures = [_serialize_model(pic) for pic in GifPictureManager.get_random_pics(how_many)]

    result = {
        'pics': gif_pictures,
    }
    return JsonResponse(result)


@api_login_required
def search(request):
    q = request.GET.get('q', None)
    if not q:
        return JsonResponse({'msg': 'missing query'}, status=400)

    q = q.split(' ')
    start = int(request.GET.get('start', 0))
    how_many = int(request.GET.get('how_many', 18))
    gif_pictures = [_serialize_model(pic) for pic in GifPictureManager.search(q, start, how_many)]

    result = {
        'pics': gif_pictures,
    }
    return JsonResponse(result)


def search_suggestions(request):
    global all_words
    q = request.GET.get('q', None)
    if not q:
        return JsonResponse({'msg': 'missing query'}, status=400)

    suggestions = GifPictureManager.get_search_suggestions(q)

    result = {
        'suggestions': suggestions,
    }
    return JsonResponse(result)
