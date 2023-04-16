from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListApi.as_view(),name='list-api'),
    path('create/', views.PostCreateApi.as_view(),name='create-api'),
    path('<int:pk>/detail',views.PostDetailApi.as_view(),name='detail-api'),
    path('<int:pk>/update',views.PostUpdateApi.as_view(),name='update-api'),
    path('<int:pk>/delete',views.PostDeleteApi.as_view(),name='delete-api'),
    path('<int:pk>/edit',views.PostEditApi.as_view(),name='edit-api'),
    path('<int:pk>/user-edit',views.UserEdit.as_view(),name='user-edit-api'),
    path('user/',views.UserList.as_view(),name='user-api'),
    path('create-user/',views.CreateUser.as_view(),name='create-user-api'),
    path('<int:pk>/profile/',views.ProfileDetailApi.as_view(),name='profile'),
    path('<int:pk>/update-profile/',views.ProfileUpdateApi.as_view(),name='update_profile'),
]
