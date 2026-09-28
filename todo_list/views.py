from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
# Create your views here.
def home(request):
    all_items = List.objects.all()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'all_items': all_items, 'form': ListForm()}
    return render(request, 'home.html', context)
def about(request):
    context = {'myName' : 'Raymart Escuadro bading'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    return redirect('home')

def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')
def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')