from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:itemno>',views.detail, name = 'detail'),
    path("new/", views.new,name="new"),
    path('<int:itemno>/delete/',views.delete, name = 'delete'),
    path('<int:itemno>/edit/',views.edit, name = 'edit'),
    path("", views.items, name="items"),

]