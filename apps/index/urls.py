from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:incorrect_data>', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
    path('register/<int:unfortunately>', views.register, name='register'),
    path('register/new/<int:superuser>', views.new, name='new')
]
