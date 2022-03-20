from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.accounts.urls import accounts_urlpatterns
from apps.notes.urls import notes_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += accounts_urlpatterns  # add URLs for authentication
urlpatterns += notes_urlpatterns  # notes URLs
