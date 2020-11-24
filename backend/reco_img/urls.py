from django.urls import path
from reco_img import views

urlpatterns = [
    path('',views.reco_img, name = 'reco_img')
]

