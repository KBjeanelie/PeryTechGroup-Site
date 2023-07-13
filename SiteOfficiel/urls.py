
from .views import contact_view
from django.urls import path

from SiteOfficiel.views import AboutView, ContactView, IndexView, ProjetView, ServiceView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', ServiceView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('projets/', ProjetView.as_view(), name='projets'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('send_message/', contact_view, name='send_message')
]