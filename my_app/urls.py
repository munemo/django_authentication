from django.conf.urls import url
from my_app import views

app_name = 'my_app'

urlpatterns = [
    url(r'^relative/', views.relative, name="relative"),
    url(r'^other/', views.other, name="other"),
    url(r'^register/', views.register, name="register"),
    url(r'^signin/', views.signin, name="signin"),
    url(r'^my_admin/$', views.my_admin, name="my_admin")
]
