from django.shortcuts import render, redirect
from .models import Book, Author, Language

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors},
    )

def about(request):
    return render(request,'about.html')

from django.views import generic
from django.db.models import Q

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        object_list = Author.objects.filter(
            Q(first_name__icontains=query)|Q(last_name__icontains=query)
        )
        return object_list


class AuthorDetailView(generic.DetailView):
    model = Author

class BookDetailView(generic.DetailView):
    model = Book


from .forms import AddBookForm
from django.contrib import messages
import isbnlib

def convert_to_isbn13(isbn):
    isbn = isbnlib.canonical(isbn)
    if(isbnlib.is_isbn10(isbn)):
        isbn13 = isbnlib.to_isbn13(isbn)
        return isbn13
    elif(isbnlib.is_isbn13(isbn)):
        return isbn
    else:
        return None

def get_book_meta(isbn):
    try:
        isbnMeta = isbnlib.meta(str(isbn), service='wiki')
        if bool(isbnMeta):
            return isbnMeta
    except:
        try:
            isbnMeta = isbnlib.meta(str(isbn), service='goob')
            if bool(isbnMeta):
                return isbnMeta
        except:
            try:
                isbnMeta = isbnlib.meta(str(isbn), service='openl')
                if bool(isbnMeta):
                    return isbnMeta
            except:
                return None

# pls dont hurt me :c
def add_book_by_isbn(request):
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            isbn = form.cleaned_data.get('isbn')
            isbn = convert_to_isbn13(isbn)
            if isbn==None:
                messages.error(request, "ISBN is bullshit like u")
            elif Book.objects.filter(isbn=isbn).exists():
                messages.error(request, "ISBN already exists")
            else:
                if request.FILES.get('bookfile', False):
                    book = Book(bookfile=request.FILES["bookfile"])
                else:
                    book = Book()
                meta = get_book_meta(isbn)
                if meta is not None:
                    book.title = meta['Title']
                    book.save()
                    if str(meta['Language']).strip() != "":
                        if Language.objects.filter(name=meta['Language']).exists():
                            book.language = Language.objects.get(name=meta['Language'])
                        else:
                            book.language = Language.objects.create(name=meta['Language'])
                    for author in meta['Authors']:
                        name = author.split(' ')
                        if Author.objects.filter(first_name=name[0]).exists():
                            book.author.add(Author.objects.filter(first_name=name[0]))
                        else:
                            book.author.add(Author.objects.create(first_name=name[0], last_name=name[1]))
                    if isbnlib.desc(isbn):
                        book.description = isbnlib.desc(isbn)
                book.isbn = isbn
                book.save()
                return redirect("/shelf/books")
        else:
            messages.error(request, "Some error occurred")
    else:
        form = AddBookForm()
    return render(request, 'shelf/book_add.html', {'form': form})
