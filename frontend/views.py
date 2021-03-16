from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest
from django import template

# Create your views here.

class OpenPpdbFrontend:

    def index(request):
        context = {"side_dashboard": "active"}
        context['segment'] = 'index'
        html_template = loader.get_template( 'index.html' )
        return HttpResponse(html_template.render(context, request))

    def formulir(request):
        context = {"side_formulir": "active"}
        html_template = loader.get_template( 'formulir.html' )
        return HttpResponse(html_template.render(context, request))

    def pages(request):
        context = {}
        try:
            load_template      = request.path.split('/')[-1]
            context['segment'] = load_template
            html_template = loader.get_template( load_template )
            return HttpResponse(html_template.render(context, request))
        except template.TemplateDoesNotExist:
            html_template = loader.get_template( '404.html' )
            return HttpResponseBadRequest(html_template.render(context, request), status=404)
        except:
            html_template = loader.get_template( '500.html' )
            return HttpResponseBadRequest(html_template.render(context, request), status=500)

    def login(request):
        context = {}
        html_template = loader.get_template( 'login.html' )
        return HttpResponse(html_template.render(context, request))

    def register(request):
        context = {}
        html_template = loader.get_template( 'register.html' )
        return HttpResponse(html_template.render(context, request))

    def forgot_password(request):
        context = {}
        html_template = loader.get_template( 'forgot-password.html' )
        return HttpResponse(html_template.render(context, request))

    def recovery_password(request):
        context = {}
        html_template = loader.get_template( 'recovery-password.html' )
        return HttpResponse(html_template.render(context, request))