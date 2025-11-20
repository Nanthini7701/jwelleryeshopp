from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from .views import signup_view


app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
   path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='detail'),
   path("logout/", LogoutView.as_view(next_page="logout_success"), name="logout"),
path("login/", views.login_view, name="login"),
path("signup/", views.signup_view, name="signup"),
    # Password Reset URLs
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='shop/password_reset.html'),
         name='password_reset'),

    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='shop/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'),
         name='password_reset_complete'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
      path('about/', views.about, name="about"),
   path("contact/", views.contact, name="contact"),
      path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:pk>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('', views.index, name='home'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
]
