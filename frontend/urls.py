from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('about', views.about),
    path('news', views.news),
    path('podcast', views.podcast),
    path('store', views.store)
]