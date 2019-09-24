from django.urls import path
from . import views

app_name = 'booksite'

urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("book",views.bookform, name="bookform1"),
    
]