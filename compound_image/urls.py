from django.urls import path

from compound_image import views

urlpatterns = [path("<str:smiles>", views.generate_image, name="compound-image")]
