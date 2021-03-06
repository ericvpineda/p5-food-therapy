from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('event_categories', views.event_categories, name="event_categories"),
    path('event_create', views.event_create, name="event_create"),
    path('event_forum', views.event_forum, name="event_forum"),
    path('event/<int:id>/', views.event, name="event"),
    path('event_join', views.event_join, name="event_join"),
    path('food_browse', views.food_browse, name="food_browse"),
    path('food_detail', views.food_detail, name="food_detail"),
    path('food_list', views.food_list, name="food_list"),
    path('future_food_event', views.future_food_event, name="future_food_event"),
    path('event_add_confirmation', views.event_add_confirmation, name="event_add_confirmation"),
    path('event_create_confirmation', views.event_create_confirmation, name="event_create_confirmation"),
    path('food_add_confirmation', views.food_add_confirmation, name="food_add_confirmation"),
    
    path('', views.title, name="title"),
]
