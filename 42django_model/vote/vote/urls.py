"""vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from polls import views
from vote import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_subjects),
    # path('api/subjects/',views.api_show_subjects),
    path('api/', include('polls.urls')),
    path('api/teachers/',views.api_show_teachers),
    path('teachers/<int:sno>/', views.show_teachers, name='teachers'),
    path('praise/<int:tno>/', views.praise_or_criticize, name='praise'),
    path('criticize/<int:tno>/', views.praise_or_criticize, name='criticize'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('captcha/', views.get_captcha, name='captcha'),
    path('excel/', views.export_teachers_excel, name='excel'),
    path('teachers_data/', views.get_teachers_data, name='teachers_data'),
    path('chart/',views.get_teachers_chart,name='chart'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))

