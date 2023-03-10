from django.urls import path
from vacancies.views import CatListCreateView, CategoryDetailView

urlpatterns = [
    path("", CatListCreateView.as_view()),
    path("<int::pk>", CategoryDetailView.as_view()),
]