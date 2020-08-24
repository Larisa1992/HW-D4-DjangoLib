from django.contrib import admin #специальный блок admin, который позволяет регистрировать моделей для панели администратора
from p_library.models import Book, Author, Publishing

#  Django создаст для нашей модели Book структуру панели по умолчанию благодаря наследованию admin.ModelAdmin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display= ('title','author', 'publishing') #список отображаемых полей модели Book в режиме списка
    
    # @staticmethod
    # def author_full_name(obj):
    #     return obj.author.full_name

    # list_display = ('title', 'author_full_name',)

#каждая модель находится в своем зарегистрированном application-блоке
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    list_display= ('name','year_foundation')