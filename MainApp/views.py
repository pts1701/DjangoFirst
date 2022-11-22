from django.shortcuts import render, HttpResponse
from django.http import Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request, 'index.html')

def item_id(request, item_id):
    # items = Item.objects.all()
    # for item in items:
    #     if item.id == item_id:
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={item_id} не найден")
    context = {
        "item": item
    }
    return render(request, 'item.html', context)
    # raise Http404(f"Товар с id={item_id} не найден")

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
