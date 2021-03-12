import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django import template

# Create your views here.

class OppdbBackend:

    def index(request):
        data = {
                "code": 200,
                "message": "OK",
                "data": None
            }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    def pages(request):
        context = {}
        try:
            load_template      = request.path.split('/')[-1]
            context['segment'] = load_template
            html_template = loader.get_template( load_template )
            return HttpResponse(html_template.render(context, request))
        except template.TemplateDoesNotExist:
            data = {
                "code": 404,
                "message": "Not Found",
                "data": None
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        except:
            data = {
                "code": 500,
                "message": "Server Errors",
                "data": None
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')