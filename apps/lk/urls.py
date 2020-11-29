from django.urls import path
from . import views

app_name = 'lk'
urlpatterns = [
    path('<str:user_login>', views.index, name="index"),
    path('<str:user_login>/history', views.view_history, name="view_history"),
    path('<str:user_login>/settings', views.settings, name="settings"),
    path('<str:user_login>/wait', views.wait, name="wait"),
    path('<str:user_login>/newPhoto', views.newPhoto, name="newPhoto"),
    path('<str:user_login>/newPhoto/<str:foodName>/<str:foodDescription>', views.chooseFood, name="chooseFood"),
    # path('<str:user_login>/upload_image', views.upload_image, name="upload_image"),
]
