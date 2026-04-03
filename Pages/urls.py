from django.contrib import admin
from django.urls import path,include
from .views import HomeView, GameListView, DevlogView, ManifestoView, ContactView

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("games/",GameListView.as_view(),name="game_list"),
    path("devlog/",DevlogView.as_view(),name="devlog"),
    path("manifesto/",ManifestoView.as_view(),name="manifesto"),
    path("contact/",ContactView.as_view(),name="contact"),
]