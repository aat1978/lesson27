from django.urls import path
from vacancies.views import root

urlpatterns = [
    path("", root),
]
