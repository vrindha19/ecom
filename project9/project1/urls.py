from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),
     path('index/', views.index, name='index'),
     path('fruits/', views.fruits, name='fruits'),
      path('vegitables/', views.vegitables, name='vegitables'),
       path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
         path('payment/', views.payment, name='payment'),
         path('contact/', views.contact, name='contact'),
        path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
        path('view_product/', views.view_product, name='view_product'),
         path('forgot_password/', views.forgot_password, name='forgot_password'),
        path('about/', views.about, name='about'),
         path('view_order/', views.view_order, name='view_order'),
        path('orderpage/', views.orderpage, name='orderpage'),

         
]
