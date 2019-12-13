from django.urls import path
from . import views
  
urlpatterns = [
    path('list/', views.UserViewSet.list, name='list'),
    path('retrieve/<int:pk>', views.UserViewSet.retrieve, name='retrieve'),
     

]