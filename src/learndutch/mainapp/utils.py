'''
Created on May 25, 2011

@author: jagadeesh
'''

from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin, SingleObjectTemplateResponseMixin
from django import http
from django.utils import simplejson as json

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



class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

    def render_success(self, message, result=''):
        context = {'success': True, 'message': [message], 'result': result}
        return self.render_to_response(context)

    def render_error(self, message):
        if type(message) == str:
            message = [message]
        context = {'success': True, 'message': [message], 'result': {}}
        return self.render_to_response(context)
