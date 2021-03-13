from django.urls import path, re_path
from frontend.views import OpenPpdbFrontend

urlpatterns = [

    # The home page
    path('', OpenPpdbFrontend.index, name='home'),
    path('login/', OpenPpdbFrontend.login, name='login'),
    path('register/', OpenPpdbFrontend.register, name='register'),
    path('forgot-password/', OpenPpdbFrontend.forgot_password, name='forgot-password'),
    path('recovery-password/', OpenPpdbFrontend.recovery_password, name='recovery-password'),
    path('formulir/', OpenPpdbFrontend.formulir, name='formulir'),

    # Matches any html file
    re_path(r'^.*\.*', OpenPpdbFrontend.pages, name='pages'),

]