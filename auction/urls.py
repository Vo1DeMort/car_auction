from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin site
    path("admin/", admin.site.urls),

    # allauth 
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),

    # local apps
    path("",include("core.urls")),
]
