try:
    from django.http import JsonResponse
except ImportError:
    import json
    from django.http import HttpResponse

    def JsonResponse(response_data, *args, **kwargs):
        return HttpResponse(json.dumps(response_data), *args, mimetype='application/json', **kwargs)
