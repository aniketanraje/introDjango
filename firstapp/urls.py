from django.urls import path

from . import views

urlpatterns = [
    path("http-response/", views.hello, name="hello"),
    path("", views.hello_from_html, name="html"),
    # path("add/", views.add, name="add"), #uncomment for explaination
    path("add", views.add, name="add"), #works with post
]

#Note
#You called this URL via POST, but the URL doesn't end in a slash
# and you have APPEND_SLASH set.
# Django can't redirect to the slash URL while maintaining POST data.
# Change your form to point to 127.0.0.1:8000/add/ (note the trailing slash),
# or set APPEND_SLASH=False in your Django settings.
