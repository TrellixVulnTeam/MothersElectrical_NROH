from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# ---------------------------------
def index(request):
    return render(request,'index.html')

# ---------------------------------
def contactus(request):
    return render(request,'contactus.html')

# ---------------------------------
def aboutus(request):
    return render(request,'aboutus.html')

# ---------------------------------
def product(request):
    return render(request,'product.html')

# ---------------------------------
def retailers(request):
    return render(request,'retailer.html')
