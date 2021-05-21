from django.urls import re_path, path

from .views import ProcessingDataListView, post_category_view, edit_category_view

urlpatterns = [
    re_path(r"^list_all/", ProcessingDataListView.as_view(), name="list-all"),
    path("create/", post_category_view, name="create"),
    path("edit/<pk>/", edit_category_view, name="edit"),
]
