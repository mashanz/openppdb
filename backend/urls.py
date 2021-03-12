from django.urls import path, re_path
from backend.views import OppdbBackend

urlpatterns = [

    # The home page
    path('api', OppdbBackend.index, name='backend'),

    # Matches any html file
    re_path(r'^.*\.*', OppdbBackend.pages, name='forbidden'),

]