from django.urls import path, re_path
from backend.views import OppdbBackend

urlpatterns = [

    # The home page
    path('', OppdbBackend.index, name='backend'),
    path('login', OppdbBackend.login, name='login'),

    # Matches any html file
    re_path(r'^.*\.*', OppdbBackend.pages, name='forbidden'),

]