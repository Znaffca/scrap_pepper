from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rtv-new/", views.SearchRtvView.as_view(), name="rtv_new"),
    path("pc-new/", views.SearchPcView.as_view(), name="pc_new")
]
