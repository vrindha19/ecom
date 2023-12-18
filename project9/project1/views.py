from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# def members(request):
#     return render(request,'index2.html')
def home(request):
    return render(request,'index.html')
def fruits(request):
    return render(request,'fruits.product.html')
def vegitables(request):
    return render(request,'vegitables.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def payment(request):
    return render(request,'view_payment.html')
def contact(request):
    return render(request,'contact.html')
def add_product(request):
    return render(request,'add_product.html')
def shopping_cart(request):
    return render(request,'shopping cart.html')
def view_product(request):
    return render(request,'view_product.html')
def forgot_password(request):
    return render(request,'forgot_password.html')
def about(request):
    return render(request,'about.html')
def view_order(request):
    return render(request,'view_orders.html')
def orderpage(request):
    return render(request,'orderpage.html')
def add_product(request):
    return render(request,'add_product.html')
def logout(request):
    return render(request,'logout.html')
def logout_action(request):
    return render(request,'logout-action.html')
def orderpage(request):
    return render(request,'orderpage.html')
