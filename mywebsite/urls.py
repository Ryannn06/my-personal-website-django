from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('account/', include('django.contrib.auth.urls')),
	path('', views.index, name="home"),
	path('myprojects/', views.my_projects, name="my_projects"),
	path('create_project/', views.create_project, name="create_project"),
	path('accounts/login/', views.user_login, name="login"),
	path('accounts/register/', views.register, name="register"),
	
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)