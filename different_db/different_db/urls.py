"""different_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1 import views
router=DefaultRouter()
#router.register('',views.Viewset_Emp)
#router.register('',views.Viewset_Details)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('save/',views.save_details,name='save'),
    path('show_all/',views.show_detalis,name='show_details'),
    path('update/',views.update_details,name='update'),
    path('delete/',views.delete_details,name='delete'),
    path('api/',views.Student_serial.as_view()),
    path('api/<int:idno>/',views.Student_details.as_view()),
    path('search/',views.search, name = 'search')
]
