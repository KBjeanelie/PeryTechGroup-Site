
from django.urls import path

from SiteOfficiel.views import AboutView, ContactView, IndexView, ProjetView, ServiceView


urlpatterns = [
    path('', IndexView.as_view()),
    path('services/', ServiceView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('projets/', ProjetView.as_view(), name='projets'),
    path('contact/', ContactView.as_view(), name='contact'),
]