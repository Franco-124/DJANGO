# my_first_app/views.py

from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, Author,Profile
from django.views.generic.base import TemplateView
# Vista de lista de carros
def car_list(request):
    cars = Car.objects.all()  # Obtener todos los carros
    return render(request, 'my_first_app/car_list.html', {'cars': cars})

# Vista de lista de autores
def author_list(request):
    authors = Author.objects.all()  # Cambiar a 'authors'
    return render(request, 'my_first_app/author_list.html', {'authors': authors})

def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    author = Author.objects.get(id=kwargs['id'])
    profile = Profile.objects.get(author_id=kwargs['id'])
    return HttpResponse(f"Author: {author.name} - Profile biography {profile.biography} website {profile.website}")


class CarListView(TemplateView):
    

    def get_context_data(self):
        context = super().get_context_data()
        context['cars'] = Car.objects.all()
        return context







def my_test_view(request , *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")


