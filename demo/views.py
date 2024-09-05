# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from .models import Book
# from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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

# def first(request):
#     books = Book.objects.all()
#
#
#     return render(request, 'first_temp.html', {'books': books})


#so we are creating a builtin view for our books that will use all power of django and create option like HTTP methods for us
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
