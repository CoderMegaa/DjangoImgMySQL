from django.shortcuts import render, redirect
from myapp.forms import ImageForm
from django.http import HttpResponse
from myapp.models import Image
# Create your views here.

def indexPage(request,*args, **kwargs):
    image = Image.objects
    if request.method == 'POST':
       form = ImageForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('/')
    else:
        form = ImageForm()
        context = {
            'form':form,
            'image':image
        }
               
    return render(request,'index.html',context)
