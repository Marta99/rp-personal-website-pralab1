from django.urls import path
from apps.portfolio import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>', views.project_detail, name='project_detail'),

]