from django.urls import path
from plan import views

urlpatterns = [
    path('', views.plan, name='plans'),
    path('<int:id>/', views.plan_id, name='plan_id'),
]
