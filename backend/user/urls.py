from django.urls import path

from user import views

urlpatterns = [
    path('token/', views.token, name='token'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout,name='signout'),
]
