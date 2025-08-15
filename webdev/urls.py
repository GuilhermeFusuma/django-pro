from django.contrib import admin
from mycontacts import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show, name="show"),
    path('add/', views.add),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('edit/<int:pk>/', views.edit, name="edit")
]