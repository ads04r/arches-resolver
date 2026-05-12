from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, Http404, HttpResponseRedirect
from arches.app.views.plugin import PluginView

class ResolverMain(PluginView):

    def get(self, request):
        return JsonResponse({"datasets": []})