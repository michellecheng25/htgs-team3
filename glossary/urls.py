from django.urls import path

from glossary import views


urlpatterns = [
  path("", views.index, name="glossary")
]