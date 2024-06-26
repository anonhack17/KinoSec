"""
URL configuration for KinoSecBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from security_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('system/<int:system_pk>/add_atack/', views.add_atack, name='add_atack'),
    path('atack/<int:atack_pk>/edit/', views.edit_atack, name='edit_atack'),
    path('atack/<int:atack_pk>/delete/', views.delete_atack, name='delete_atack'),
    path('system/<int:pk>/add_copyright/', views.add_copyright, name='add_copyright'),
    path('system/<int:pk>/edit_copyright/', views.edit_copyright, name='edit_copyright'),
    # Изменение авторских прав
    path('edit_copyright/<int:copyright_id>/', views.edit_copyright, name='edit_copyright'),
    path('system/<int:pk>/', views.system_detail, name='system_detail'),
    path('security_events_list/', views.security_events_list, name='security_events_list'),  # Добавленный маршрут
    path('edit_system/<int:system_id>/', views.edit_system, name='edit_system'),
    path('system/<int:pk>/', views.system_detail, name='system_detail'),
    path('add_system/', views.add_system, name='add_system'),
    path('add_security_event/', views.add_security_event, name='add_security_event'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('systems_list/', views.systems_list, name='systems_list'),
    path('delete_system/<int:system_id>/', views.delete_system, name='delete_system'),

]
