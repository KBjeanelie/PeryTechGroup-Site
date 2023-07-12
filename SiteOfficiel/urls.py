
from django.urls import path

from SiteOfficiel.views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
]