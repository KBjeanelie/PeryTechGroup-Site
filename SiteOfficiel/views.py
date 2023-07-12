from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class AboutView(View):
    template_name = "pages/about.html"

    def get(self, request):
        return render(request, self.template_name)

class ServiceView(View):
    template_name = "pages/service.html"

    def get(self, request):
        return render(request, self.template_name)

class ProjetView(View):
    template_name = "pages/project.html"

    def get(self, request):
        return render(request, self.template_name)

class ContactView(View):
    template_name = "pages/contact.html"

    def get(self, request):
        return render(request, self.template_name)