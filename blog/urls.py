from django.urls import path
from .  import views 
urlpatterns = [
    path('',views.index,name='blogpost'),
    path('blogpost/<int:id>/',views.blogpost,name='blogpost')

         ]
