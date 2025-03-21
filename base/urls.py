from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('edit_profile/', views.editProfile, name='edit-profile'),

    path('create/', views.createPost, name='create-post'),
    path('add_category/', views.addCategory, name='add-category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)