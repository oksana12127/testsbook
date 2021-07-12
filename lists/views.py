from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


# Create your views here.

# def home_page(request):
#     '''домашняя страница'''
#     return render(request, 'home.html')

# def home_page(request):
#     '''домашняя страница'''
#
#
#     if request.method == 'POST':
#         return HttpResponse(request.POST['item_text'])
#     return render(request, 'home.html')

# def home_page(request):
#     '''домашняя страница'''
#     item = Item()
#     item.text = request.POST.get('item_text', '')
#     item.save()
#     return render(request, 'home.html', {
#         'new_item_text': item.text
#     })

def home_page(request):
    '''домашняя страница'''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
