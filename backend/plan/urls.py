from django.urls import path
from plan import views

urlpatterns = [
    path('<int:id>/', views.get_plan_id, name='get_plan_id'),
]
