import os
import django
from fastapi import FastAPI
# Konfiguracja Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()


# Teraz możesz importować modele Django
from core.models import *  # lub konkretne modele, np: from core.models import Book, Author

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def root(name):
    return {"message": f"Hello {name}"}

# Przykład endpointu wykorzystującego modele Django
@app.get("/books/")
def get_books():
    from django.forms.models import model_to_dict
    books = Book.objects.all()
    return [model_to_dict(book) for book in books]