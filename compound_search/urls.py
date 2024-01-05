from django.urls import path
from compound_search import views


urlpatterns = [
    path("", views.search, name="search-compounds"),
    path("add-compounds", views.add_compounds, name="add-compounds"),
]
