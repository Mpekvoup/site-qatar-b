from django.urls import path, include
from main.views import index, switch_language

urlpatterns = [
    path("",             index,           name="index"),
    path("i18n/",        include("django.conf.urls.i18n")),
    path("switch-lang/", switch_language, name="switch_language"),
]
