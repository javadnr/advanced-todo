from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('<int:pk>/detail/',views.PostModelDetailView.as_view(),name='post_detail'),
    path('', views.PostModelListView.as_view(),name="list"),
    path('new/',views.PostCreateView.as_view(),name="create"),
    path('<int:pk>/update/', views.PostUpdateView.as_view(),name="post_update"),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name="post_delete"),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LogInView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('password_change/',views.PasswordChange.as_view(),name='password_change'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    # path('profile-edit/<int:pk>/',views.ProfileEditView.as_view(),name='edit_profile'),
    # path('create_profile',views.CreateProfileView.as_view(),name='create_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)