from .json_compat import JsonResponse


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = self.get_json_data()
            return JsonResponse(data)
        else:
            return response

    def get_json_data(self, action=None):
        object_str = str(self.object)
        data = {
            'pk': self.object.pk,
            'success': True,
            'object': object_str,
            'action': action,
            'message': object_str
        }
        if action:
            data['message'] = "%s %s" % (object_str, action.upper())
        return data
