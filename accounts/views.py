from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from .forms import MyForm

def index(request):   #r
  objects  = Todo.objects.all()
  context = {
    'objects':objects,
  }
  return render(request,'accounts/index.html',context)



def delete(request,id):  #d
  object  = get_object_or_404(Todo,id=id)
  object.delete()
  return redirect('/')



def create(request):   #c
  if request.method=='POST':
    form = MyForm(request.POST or None)
    if form.is_valid():
     form.save()
     return redirect('/')
  else:
    form = MyForm()  
  context = {
    'form':form,
  }  
  return render(request,'accounts/create.html',context)



def edit(request,id):  #r
  object  = get_object_or_404(Todo,id=id)
  if request.method == 'POST':
    form = MyForm(request.POST,instance=object)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
    form = MyForm(instance=object)
    context = {
    'form':form,
    }  
  return render(request,'accounts/edit.html',context)    