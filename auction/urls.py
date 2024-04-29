from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin site
    path("admin/", admin.site.urls),

    # allauth 
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),

    # local apps
    path("",include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
