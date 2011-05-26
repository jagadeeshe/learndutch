'''
Created on May 25, 2011

@author: jagadeesh
'''

from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin, SingleObjectTemplateResponseMixin

class SignleObjectExtraContextMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        extra = self.get_extra_context_data()
        context = SingleObjectMixin.get_context_data(self, **kwargs)
        context.update(extra)
        return context

class BaseCustomDetailView(SignleObjectExtraContextMixin, View):
    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class CustomDetailView(SingleObjectTemplateResponseMixin, BaseCustomDetailView):
    pass

