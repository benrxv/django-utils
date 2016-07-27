from django.views import generic
from .mixins import AjaxableResponseMixin


class CreateView(AjaxableResponseMixin, generic.CreateView):

    def get_json_data(self):
        return super(CreateView, self).get_json_data(action="created")


class UpdateView(AjaxableResponseMixin, generic.UpdateView):

    def get_json_data(self):
        return super(UpdateView, self).get_json_data(action="updated")


class DeleteView(AjaxableResponseMixin, generic.DeleteView):

    def get_json_data(self):
        return super(DeleteView, self).get_json_data(action="deleted")
