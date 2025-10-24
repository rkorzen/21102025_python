from django.shortcuts import render
from .models import PythowaKlasa, Book
# Create your views here.
from django.http import HttpResponse, JsonResponse


def hello(request, name="World"):
    return render(
        request,
        "hello.html",
        {"name": name}
    )


def suma(request, a, b):
    # return HttpResponse(f"<p>{a} + {b} = {a + b}</p>")
    return render(
        request,
        "base.html",
        {
            "a": a, "b": b, "suma": a + b, "pokaz": True, "dane": [1, 2, 3, "a", "b", "c"],
            "klasa": PythowaKlasa
        }
    )


def book_list(request):
    return render(
        request,
        "core/book_list.html",
        context={"books": Book.objects.all()}
    )


def api_book_list(request):
    books = Book.objects.all()
    books_json = [vars(book) for book in books]
    for book in books_json:
        book.pop("_state")
        book["created_at"] = book["created_at"].strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse(books_json, safe=False)


