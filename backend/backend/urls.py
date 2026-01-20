from django.contrib import admin
from django.urls import path, include  # ✅ THÊM include

urlpatterns = [
    path("", lambda request: None),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
