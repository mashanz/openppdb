import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django import template
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class OppdbBackend:

    @csrf_exempt
    def index(request):
        data = {
                "code": 200,
                "message": "OK",
                "data": None
            }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    @csrf_exempt
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
                "message": "Page Not Found",
                "data": None
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        except:
            data = {
                "code": 500,
                "message": "Internal Server Errors",
                "data": None
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')

    @csrf_exempt
    def login(request):
        if request.method == "POST":
            data = {
                "code": 200,
                "message": "OK",
                "data": None
            }
            
        else:
            data = {
                "code": 403,
                "message": "Forbidden Access",
                "data": None
            }
        
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')
