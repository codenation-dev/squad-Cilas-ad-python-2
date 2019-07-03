from django.contrib import admin
from django.urls import include, path
from televendas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('televendas.urls'))
]

