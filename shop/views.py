from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
import json

def mainpage(request):
    return render(request, 'shop/mainpage.html', {'text':"This is the main returning page!"})

def items(request, shop_pk, category_pk):
    item_list = Item.objects.filter(category=category_pk, store=shop_pk)
    try:
        return render(request, 'shop/category.html', {'item_list':item_list})
    except ValueError:
        return render(request, 'shop/error.html', {'items':item_list, 'error':'No such a shop!'})

def createitem(request):
    if request.method == 'GET':
        return render(request, 'shop/create.html', {'form':ItemForm()})
    else:
        try:
            form = ItemForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.save()
            return redirect('createitem')
        except ValueError:
            return render(request, 'shop/mainpage.html', {'text':"This is the main returning page!"})

def oneitem(request, shop_pk, category_pk, item_pk):
    item = Item.objects.filter(category=category_pk, store=shop_pk)[item_pk-1]
    if request.method == 'GET':
        form = ItemForm(instance=item)
        return render(request, 'shop/oneitem.html', {'item':item})
    try:
        form = ItemForm(request.POST, instance=item)
        form.save()
        return redirect('oneitem')
    except ValueError:
        return render(request, 'shop/error.html', {'items':item, 'error':'No such a shop!'})

