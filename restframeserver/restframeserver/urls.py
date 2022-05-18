from django.urls import path
from django.conf.urls import include
from users import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.users_list),
    path('users/<int:user_num>/', views.users),
    path('app_login/', views.app_login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
