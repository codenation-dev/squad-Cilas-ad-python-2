from django.urls import include, path
from televendas import views

urlpatterns = [
    path("api/", include('televendas.urls'))
]
