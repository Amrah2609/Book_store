from django.shortcuts import render, redirect
from core.models import IndexPage, BookCategory, CategorySection, AboutPage, ContactMessage
from core.forms import ContactForm
from django.contrib import messages
# Create your views here.


def index(request):
    about = AboutPage.objects.first()
    section = CategorySection.objects.first()
    categories = BookCategory.objects.all()
    content = {"index_pages": IndexPage.objects.all(),
    "about": about,
    "section": section,
    "categories": categories,
    }
    return render(request, "index.html", content)


def about(request):
    content = {"about": AboutPage.objects.first()}
    return render(request, "about.html", content)


def categories(request):
    section = CategorySection.objects.first()
    content = {
        "section": section,
        "categories": BookCategory.objects.all(),}
    return render(request, "categories.html", content)


def blog(request):
    return render(request, "blog.html")


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesaj göndərildi.")
            return redirect("contact")
    content = {
        "form": form,

    }
    return render(request, "contact.html", content)


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
