from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, Publishing

def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all().order_by('publishing')
    books.order_by('publishing')
    arr = [i for i in range(1, 101)]
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
        "arr": arr,
    }
    return HttpResponse(template.render(biblio_data, request)) #requestдобавлен в рендеринг, чтобы при открытии сайта в форму добавится CSRF

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def publishing(request):
    template = loader.get_template('publishing.html')
    publishing = Publishing.objects.all()
    publishing_data = {
        "publishing": publishing,
    }
    return HttpResponse(template.render(publishing_data))
