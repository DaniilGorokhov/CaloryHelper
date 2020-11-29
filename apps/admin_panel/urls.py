from django.urls import path
from . import views

app_name = 'admin_panel'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:admin_login>/', views.index, name='index'),
    path('<str:admin_login>/spez-course', views.to_spez, name='to_spez'),
    path('<str:admin_login>/spez-course/<int:course_id>', views.edit_depends, name='edit_depends'),
    path('<str:admin_login>/spez-course/<int:course_id>/save_depends', views.save_depends, name='save_depends'),
    path('<str:admin_login>/spez-course/<int:course_id>/add_spec', views.add_spec, name='add_spec'),
    path('<str:admin_login>/add_course', views.add_course, name='add_course'),
    path('<str:admin_login>/<int:course_id>/', views.course, name='course'),
    path('<str:admin_login>/<int:course_id>/add_topic', views.add_topic, name='add_topic'),
    path('<str:admin_login>/<int:course_id>/delete_course', views.delete_course, name='delete_course'),
    path('<str:admin_login>/<int:course_id>/<int:topic_id>/', views.topic_edit, name='topic_edit'),
    path('<str:admin_login>/<int:course_id>/<int:topic_id>/delete_topic', views.delete_topic, name='delete_topic'),
    # path('<str:admin_login>/<int:course_id>/<int:topic_id>/', views.topic_edit, name='topic_edit'),
]
