from django.urls import path
from . import views
urlpatterns=[
    path('',views.watch_login),
    path('home',views.home),
    path('watch_logout',views.watch_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete),
]