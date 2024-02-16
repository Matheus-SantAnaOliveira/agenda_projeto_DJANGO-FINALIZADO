from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from agenda.models import Contact
from django.core.paginator import Paginator
from django import forms


# Create your views here.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name', 'phone',)

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(data=request.POST)
        }
        return render(request, 'agenda/create.html', context= context)
    context = {
            'form': ContactForm()
        }
    return render(request, 'agenda/create.html', context= context)
    