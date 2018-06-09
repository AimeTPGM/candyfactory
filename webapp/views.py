from django.shortcuts import render, redirect, get_object_or_404
from .models import Candy
from .forms import CandyForm

def mainpage(request):
    candies = Candy.objects.all()  
    return render(request, 'index.html', { 'candyList': candies })

def add(request):
    if request.method == "POST":
        saveCandy(request.POST, None)
        return redirect('main_page')
    else:
        form = CandyForm()
    return render(request, 'add.html', { 'candyForm': form })

def edit(request, pk):
    candy = get_object_or_404(Candy, pk=pk)
    if request.method == "POST":
        saveCandy(request.POST, candy)
        return redirect('main_page')
    else:
        form = CandyForm(instance=candy)
        return render(request, 'add.html', { 'candyForm': form })

def saveCandy(data, instance):
    if instance is None:
        form = CandyForm(data)
        candy = form.save(commit=False)
        candy.produce()
    else:
        form = CandyForm(data, instance=instance)
        candy = form.save(commit=False)
    candy.save()
