from django.urls import path
from place import views

urlpatterns = [
    path('', views.place, name = 'place'),
    path('<int:id>/', views.place_id, name = 'place_id'),
]
