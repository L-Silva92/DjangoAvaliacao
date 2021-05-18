from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories_view, name="categories"),

    path("<str:filtro_id>/filtro", views.filtro, name="filtro_id"),
    
    path("<int:product_id>", views.product, name="product_id"),

    path("createlist", views.createlist_view, name="createlist"),
    path("watchlist", views.watchlist_view, name="watchlist"),


]
