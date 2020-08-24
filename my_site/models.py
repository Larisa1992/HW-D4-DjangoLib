from django.db import models  
   
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__ (self):
        return self.full_name

class Publishing(models.Model): 
    name = models.TextField(verbose_name=("Название"))   
    year_foundation = models.SmallIntegerField(verbose_name=("Год основания")) 
    def __str__ (self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE, related_name='book_publishing', null=True, blank=True)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=("Цена"))
