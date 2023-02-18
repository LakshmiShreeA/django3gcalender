from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Book, Task
from .forms import BookForm

# Create your views here.
def index(req):
    book_list=Book.objects.all()
    context={
        "book_list":book_list
    }
    return render(req,'myapp/index.html',context)

def detail(req,book_id):
    book=Book.objects.get(id=book_id)
    return render(req,"myapp/detail.html",{"book":book})

def add_book(req):
    if req.method=="POST":
        name=req.POST.get('name',)
        desc=req.POST.get('desc',)
        price=req.POST.get('price',)
        book_image=req.FILES['book_image']

        book=Book(name=name,desc=desc,price=price,book_image=book_image)
        book.save()
    return render(req,'myapp/add_book.html')

def update(req,id):
    book=Book.objects.get(id=id)
    form=BookForm(req.POST or None,req.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(req,'myapp/edit.html',{"form":form,'book':book})

def delete(req,id):
    if req.method=="POST":
        book=Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(req,'myapp/delete.html')

def add(req):
    if req.method=="POST":
        name=req.POST.get('name',)
        desc=req.POST.get('desc',)
        start_date=req.POST.get('start_date',)
        end_date=req.POST.get('end_date',)
        start_time=req.POST.get('start_time','')
        end_time=req.POST.get('end_time','')
        book=Task(name=name,desc=desc,start_date=start_date,end_date=end_date,start_time=start_time,end_time=end_time)
        book.save()
    return render(req,'myapp/add.html')