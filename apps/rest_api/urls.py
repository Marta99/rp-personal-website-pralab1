from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryView)
router.register('posts', views.PostView, base_name='post')


urlpatterns = [
    path('token-auth/', obtain_auth_token, name='token_auth'),

    # POST /api/v1/token-auth/ HTTP/1.1
    # {
    #   "username": "admin",
    #   "password": "admin"
    # }

    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

    path('', include(router.urls)),
]