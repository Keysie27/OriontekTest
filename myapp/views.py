from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm, AddressForm

def index(request):
    return render(request, 'myapp/index.html')

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'myapp/list_clients.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm()
    return render(request, 'myapp/add_client.html', {'form': form})

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = AddressForm()
    return render(request, 'myapp/add_address.html', {'form': form})


