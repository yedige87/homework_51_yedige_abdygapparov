from django.urls import path

from webapp.views.articles import cat_view
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view),
    path('cat', cat_view),
]