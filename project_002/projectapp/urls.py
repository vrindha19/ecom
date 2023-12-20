from django.urls import path
from .views import  index, login, forgot_password, register, product_view,payment, about, contact, shopping_cart, logout_action, add_product, orderpage, view_order, vegitables, fruits,logout


urlpatterns = [
    path('', index, name='home'),
    path('fruits/', fruits, name='fruits'),
    path('vegitables/', vegitables, name='vegitables'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('payment/', payment, name='payment'),
    path('contact/', contact, name='contact'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('products/', product_view, name='products'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('about/', about, name='about'),
    path('view_order/', view_order, name='view_order'),
    path('orderpage/', orderpage, name='orderpage'),
    path('add_product/', add_product, name='add_product'),
    path('logout/', logout, name='logout'),
    path('logout_action/',logout_action, name='logout_action'),
    path('order/', orderpage, name='order'),
]
