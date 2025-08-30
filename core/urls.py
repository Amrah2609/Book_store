from django.urls import path
from .views import (
    index,
    about,
    categories,
    blog,
    contact,
    card,
    product_detail,
    checkout_page,
    login,
    register,
    search,
)

urlpatterns = [
    path("", index, name="index"),
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("categories/", categories, name="categories"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("card/", card, name="card"),
    path("product_detail/", product_detail, name="product_detail"),
    path("checkout_page/", checkout_page, name="checkout_page"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("search/", search, name="search"),
]
