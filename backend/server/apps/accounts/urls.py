from django.conf.urls import include, url


accounts_urlpatterns = [
    url(r"^api/v1/", include("djoser.urls")),
    url(r"^api/v1/", include("djoser.urls.authtoken")),
]
