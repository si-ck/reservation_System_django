from django.urls import path
from . import views  #(current folder views)
urlpatterns = [
    path('function', views.hell_world, name='home'),
    path('class',views.HelloSik.as_view())
]

