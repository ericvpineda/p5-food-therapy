from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('event_categories', views.event_categories, name="event_categories"),
    path('event_create', views.event_create, name="event_create"),
    path('event_forum', views.event_forum, name="event_forum"),
    path('event', views.event, name="event"),
    path('food_browse', views.food_browse, name="food_browse"),
    path('food_detail', views.food_detail, name="food_detail"),
    path('food_list', views.food_list, name="food_list"),
]