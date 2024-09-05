from django.db import models

# Create your models here.


#something extra information related to that particular book
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):

    # STATUSES = (
    #     (0, 'Unknown'),
    #     (1, 'processed'),
    #     (2, 'paid')
    # )

    # title = models.CharField(null=True, blank=False, unique=True,
    #                          default='', choices=STATUSES)

    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    # price = models.FloatField(default=0, max_digits=0, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    # price = models.BigIntegerField(default=0)

    # published = models.DateField(auto_now=True, auto_now_add=True)
    # published = models.TimeField(auto_now=True, auto_now_add=True)
    # published = models.DateTimeField(auto_now=True, auto_now_add=True)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    # cover = models.FileField(upload_to='covers')
    cover = models.ImageField(upload_to='covers', blank=True)

    # To integrate our new field

    number = models.OneToOneField(BookNumber, null=True,
                                  blank=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')



class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')


