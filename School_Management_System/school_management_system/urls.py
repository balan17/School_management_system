"""
URL configuration for school_management_system project.

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

from core import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.opening,name='home'),
    path('admin_log', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('create_student/', views.create_student, name='create_student'),
    path('login/', views.staff_login, name='staff_login'),
    path('login_student/', views.student_login, name='student_login'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('all_staffs/', views.all_staffs, name='all_staffs'),
    path('update_staff/<int:staff_id>/', views.update_staff, name='update_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('all_students/', views.all_students, name='all_students'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
