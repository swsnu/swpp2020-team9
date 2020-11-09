from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.get_location_id, name='get_location_id'),
]
