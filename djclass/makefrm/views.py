from django.shortcuts import render
from .forms import TeachForm
# Create your views here.
def teach(request):
    form=TeachForm(request.POST,request.FILES)
    if form.is_valid():
            form.save()
            form=TeachForm()

    return render(request,"index.html",{
            'form':form
    })