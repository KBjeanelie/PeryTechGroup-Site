from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail

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

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Envoie l'e-mail
        send_mail(
            'Nouveau message de contact',
            f'Nom: {name}\nEmail: {email}\nMessage: {message}',
            email,
            ['elijahwalter2018@gmail.com'],  # Remplacez par votre adresse e-mail de réception
            fail_silently=False,
        )

        # Renvoyer le texte de succès
        return HttpResponse('Message envoyé avec succès :)')

    return render(request, 'contact') 
