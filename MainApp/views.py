from django.shortcuts import render, HttpResponse
from django.http import Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
author = {
    "sh_name": "Zubko P.V.",
    "name": "Pavel",
    "f_name": "Vadimovich",
    "surname": "Zubko",
    "ph_num": +79263017466,
    "email": "pts1701@gmail.com"
}


# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]

item_url = "http://127.0.0.1:8000/item/"

# Create your views here.
def home(request):
    return render(request, 'index.html')

# def about(request):
#     context = {
#         "author": author
#     }
#     return render(request, 'about.html', context)

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
