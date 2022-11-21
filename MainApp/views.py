from django.shortcuts import render, HttpResponse
from django.http import Http404
author = {
    "sh_name": "Zubko P.V.",
    "name": "Pavel",
    "f_name": "Vadimovich",
    "surname": "Zubko",
    "ph_num": +79263017466,
    "email": "pts1701@gmail.com"
}


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

item_url = "http://127.0.0.1:8000/item/"

# Create your views here.
def home(request):
    text = f"""
    <h1>{"Изучаем django"}</h1>
    <strong>{author['sh_name']}</strong>    
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя: <b>{author['name']}</b><br>
    Отчество: <b>{author['f_name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    телефон: <b>{author['ph_num']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)

def item_list(request, item_id):
    text = ''
    for el in items:
        if el["id"] == item_id:
            text = f"""
            Товар: {el['name']}<br> 
            Кол-во: {el["quantity"]}
            """
            return HttpResponse(text)
    raise Http404(f"Товар с id={id} не найден")

def items_list(request):
    text = "<ol>"
    for item in items:
        text += f"<li><a href ={item_url}{item['id']}>{item['name']}</a></li>"
    text += "</ol>"
    return HttpResponse(text)