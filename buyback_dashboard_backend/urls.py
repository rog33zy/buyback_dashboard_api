from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from buyback_data import urls as buyback_urls
from processing_data import urls as processing_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/buyback/", include(buyback_urls)),
    path("api/processing/", include(processing_urls)),
]
