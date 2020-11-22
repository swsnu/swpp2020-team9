from django.urls import path

from . import views

urlpatterns = [
    path('', views.location, name = 'location'),
    path('<int:id>/', views.location_id, name='get_location_id'),
]
