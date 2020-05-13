from django.shortcuts import render
from management.models import Book
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.urls import reverse
import time
# Create your views here.
def index(request):
	book=Book.objects.all()
	context={'books':book}
	return render(request,'management/index.html',context )
def add_book(request):
	if request.method =='POST':
		new_book=Book(
				name=request.POST.get('name',''),
				author=request.POST.get('author',''),
				category=request.POST.get('category',''),
				price=request.POST.get('price',''),
				publish_date=request.POST.get('publish_date'),
				create_datetime=request.POST.get('create_datetime'),
			)
		new_book.create_datetime=time.strftime('%Y%m%d%H%I')
		new_book.save()
		return HttpResponseRedirect(reverse('management:index'))
	return render(request,'management/add_book.html')
def add_image(request):
	if request.method == 'POST':
		new_image=Image(
				name=request.POST.get('name',''),
				description=request.POST.get('description',''),
				img=request.POST.get('imag',''),
				book=request.POST.get('book',''),
			)
		new_image.save()
		return HttpResponseRedirect(reverse('management:index'))
	return render(request,'management/add_image.html',{'books':Book.objects.all()})
def book_list(request,category):
	books=Book.objects.filter(category=category)
	return render(request,'management/book_list.html',{'books':books})
def content(request,book_id):
	book=Book.objects.get(id=book_id)
	return render(request,'management/content.html',{'book':book})
def edit_book(request,book_id):
	book=Book.objects.get(id=book_id)
	if request.method =='POST':
		book.author=request.POST.get('author','')
		book.price=request.POST.get('price','')
		book.publish_date=request.POST.get('publish_date','')
		book.category=request.POST.get('category','')
		book.save()
		return HttpResponseRedirect(reverse('management:index'))
	return render(request,'management/edit_book.html',{'book':book})
def delete(request,book_id):
	book=Book.objects.get(id=book_id)
	book.delete()
	return HttpResponseRedirect(reverse('management:index'))