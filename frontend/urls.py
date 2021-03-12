from django.urls import path, re_path
from frontend.views import OpenPpdbFrontend

urlpatterns = [

    # The home page
    path('', OpenPpdbFrontend.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', OpenPpdbFrontend.pages, name='pages'),

]