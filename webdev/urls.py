from django.contrib import admin
from mycontacts import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
    path('add/', views.add),
]