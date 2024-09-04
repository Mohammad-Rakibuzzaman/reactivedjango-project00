from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

# class Another(View):
#
#     # books = Book.objects.all()
#     # books = Book.objects.filter(is_published=True)
#     book = Book.objects.get(id=1) #always brings 1 record
#
#     output = f"we have {book.title} books with ID {book.id}!!!<br>"
#
#     # output = ''
#     # for book in books:
#     #     output += f"we have {book.title} books with ID {book.id}!!!<br>"
#
#     # output = f"we have {len(books)} books in DB !!!"
#     def get(self, request):
#         # return HttpResponse('another method in class!')
#         return HttpResponse(self.output)

def first(request):
    books = Book.objects.all()


    return render(request, 'first_temp.html', {'books': books})