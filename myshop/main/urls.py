from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),  # Ensure this matches the name used in the template
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]