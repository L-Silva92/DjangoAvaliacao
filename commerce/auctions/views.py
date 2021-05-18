from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Bid, Lance, User, leilao, categ


def index(request):
    return render(request, "auctions/index.html",{
        "teste": leilao.objects.all()
    })

<<<<<<< HEAD
def watchlist_view(request):
    return render(request, "auctions/watchlist.html")

=======
>>>>>>> 1706f1b48d4be419e377bc3e51d45a6476dc7515
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def categories_view(request):
    return render(request, "auctions/categories.html", {
        "categs": categ.objects.all()
    })

@login_required
def createlist_view(request):
    if request.method == "POST":
        teste=leilao()
        teste.titulo = request.POST["title"]
        teste.descricao = request.POST["desc"]
        teste.valor_min = request.POST["valor_m"]
        teste.catego = request.POST["cate"]
        teste.dono = request.user.username
        #form = ImageUploadForm(request.POST, request.FILES)
        #if form.is_valid():
        #    image = form.cleaned_data['image']
        #    teste.Image = image
        teste.save()
        return HttpResponseRedirect(reverse("createlist"))
    else:
        categor = categ.objects.all()

        return render(request, "auctions/createlist.html",{
            "categor": categor,
        })

<<<<<<< HEAD
=======
def watchlist_view(request):
    return render(request, "auctions/watchlist.html")

>>>>>>> 1706f1b48d4be419e377bc3e51d45a6476dc7515
def product(request, product_id):
    product = leilao.objects.get(id=product_id)
    return render(request, "auctions/product.html", {
        "product" : product,
    })

def filtro(request,filtro_id):
    filtro = leilao.objects.filter(catego=filtro_id)
    passengers = leilao.objects.all()
    return render(request, "auctions/filtro.html", {
        "filtro" : filtro,
        "passengers":passengers,
    })
