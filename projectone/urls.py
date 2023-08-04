from django.contrib import admin
from django.urls import path
from app import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.index,name="index"),
]
