from django.shortcuts import render

from core.models import IndexPage


# Create your views here.


def index(request):
    content = {"index_pages": IndexPage.objects.all()}
    return render(request, "index.html", content)


def about(request):
    return render(request, "about.html")


def categories(request):
    return render(request, "categories.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def card(request):
    return render(request, "card.html")


def product_detail(request):
    return render(request, "product_detail.html")


def checkout_page(request):
    return render(request, "checkout_page.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def search(request):
    return render(request, "search.html")
