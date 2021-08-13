from django.shortcuts import render
from.models import Products

# Create your views here.
def showProd(request):
    data=Products.objects.all()
    return render(request,"index.html",{'datapro':data})