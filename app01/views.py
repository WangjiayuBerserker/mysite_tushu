from django.shortcuts import HttpResponse,render,redirect
from app01 import models

# Create your views here.
def publisher_list(request):
    publish_list = models.Publisher.objects.all()
    return render(request, 'publisher_list2.html', {'publisher_list':publish_list})

def add_pub(request):
    if  request.method == 'POST':
        pub_id = request.POST.get('id')
        if pub_id:
            new_name = request.POST.get('name')
            edit_publisher = models.Publisher.objects.get(id=pub_id)
            edit_publisher.name = new_name
            edit_publisher.save()
            return redirect('/publisher_list/')
        pub_name = request.POST.get('name',None)
        models.Publisher.objects.create(name=pub_name)
        return redirect('/publisher_list/')
    return render(request,'add_list.html')

def del_pub(request):
    pub_id = request.GET.get('id',None)
    print(pub_id)
    if pub_id:
        del_obj = models.Publisher.objects.get(id=pub_id)
        del_obj.delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('没有你想删除的出版社！！！')

# def edit_pub(request):
#
#     if request.method == 'POST':
#         pub_id = request.POST.get('id')
#         new_name = request.POST.get('name')
#         edit_publisher = models.Publisher.objects.get(id=pub_id)
#         edit_publisher.name = new_name
#         edit_publisher.save()
#         return redirect('/publisher_list/')
#     pub_id = request.GET.get('id', None)
#     pub_obj = models.Publisher.objects.get(id=pub_id)
#     return render(request,'edit_pub.html',{'pub_obj':pub_obj})


def book_list(request):
    ret = models.Book.objects.all()
    return render(request, 'book_list2.html', {'book_list':ret})

def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('name',None)
        book_pub = request.POST.get('publisher',None)
        models.Book.objects.create(name=book_name,publisher_id=book_pub)
        return redirect('/book_list/')
    ret = models.Publisher.objects.all()
    return render(request,'add_book.html',{'publisher_list':ret})

# def del_book(request):
#     book_id = request.GET.get('id',None)
#     del_obj = models.Book.objects.get(id=book_id)
#     del_obj.delete()
#     return redirect('/book_list/')

def del_book(request,arg):
    del_obj = models.Book.objects.get(id=arg)
    del_obj.delete()
    return redirect('/book_list/')

# def edit_book(request):
#     if request.method == 'POST':
#         book_id = request.POST.get('id',None)
#         new_name = request.POST.get('name',None)
#         new_pub = request.POST.get('publisher')
#         edit_obj = models.Book.objects.get(id=book_id)
#         edit_obj.name = new_name
#         edit_obj.publisher_id = new_pub
#         edit_obj.save()
#         return redirect('/book_list/')
#     book_id = request.GET.get('id')
#     ret = models.Book.objects.get(id=book_id)
#     pub_list = models.Publisher.objects.all()
#     return render(request,'edit_book.html',{'book_msg':ret,'publisher_list':pub_list})

def edit_book(request,arg):
    if request.method == 'POST':
        book_id = request.POST.get('id',None)
        new_name = request.POST.get('name',None)
        new_pub = request.POST.get('publisher')
        edit_obj = models.Book.objects.get(id=book_id)
        edit_obj.name = new_name
        edit_obj.publisher_id = new_pub
        edit_obj.save()
        return redirect('/book_list/')
    ret = models.Book.objects.get(id=arg)
    pub_list = models.Publisher.objects.all()
    return render(request,'edit_book.html',{'book_msg':ret,'publisher_list':pub_list})

def autor_list(request):
    ret = models.Autor.objects.all()
    return render(request,'autor_list2.html',{'autor_list':ret})

def add_autor(request):
    if request.method == 'POST':
        autor_name = request.POST.get('name',None)
        book_id = request.POST.getlist('book')
        new_autor_obj = models.Autor.objects.create(name=autor_name)
        new_autor_obj.book.set(book_id)
        return redirect('/autor_list/')
    ret = models.Book.objects.all()
    return render(request,'add_autor.html',{'book_list':ret})

# def del_autor(request):
#     del_id = request.GET.get('id')
#     del_obj = models.Autor.objects.get(id=del_id)
#     del_obj.delete()
#     return redirect('/autor_list/')

def del_autor(request,arg):
    del_obj = models.Autor.objects.get(id=arg)
    del_obj.delete()
    return redirect('/autor_list/')

# def edit_autor(request):
#     if request.method == 'POST':
#         edit_id = request.POST.get('id', None)
#         new_name = request.POST.get('name',None)
#         new_book = request.POST.getlist('book',None)
#         edit_obj = models.Autor.objects.get(id=edit_id)
#         edit_obj.name = new_name
#         edit_obj.book.set(new_book)
#         edit_obj.save()
#         return redirect('/autor_list/')
#
#     edit_id = request.GET.get('id')
#     ret = models.Autor.objects.get(id=edit_id)
#     book_all = models.Book.objects.all()
#     return render(request,'edit_autor.html',{'autor_msg':ret,'book_list':book_all})

def edit_autor(request,arg):
    if request.method == 'POST':
        edit_id = request.POST.get('id', None)
        new_name = request.POST.get('name',None)
        new_book = request.POST.getlist('book',None)
        edit_obj = models.Autor.objects.get(id=edit_id)
        edit_obj.name = new_name
        edit_obj.book.set(new_book)
        edit_obj.save()
        return redirect('/autor_list/')

    ret = models.Autor.objects.get(id=arg)
    book_all = models.Book.objects.all()
    return render(request,'edit_autor.html',{'autor_msg':ret,'book_list':book_all})