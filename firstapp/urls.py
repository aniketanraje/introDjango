from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("html/", views.hello_from_html, name="html"),
    path("html/add/", views.add, name="add"),

]
