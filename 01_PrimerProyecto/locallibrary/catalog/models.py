from django.db import models

# Create your models here.
from django.utils.timezone import now


class Author(models.Model):
    name = models.CharField('Name', max_length=50)
    date_of_birth = models.DateTimeField("Date of birth", default=now, blank=True)
    date_of_death = models.DateTimeField("Date of death", default=now, blank=True)
    books = models.ManyToManyField('Book', db_table="author_book")

    def __str__(self):
        return 'The author %s that birth at %s and dies at %s has tis books: %s' % (
        self.name, self.date_of_birth, self.date_of_death, self.books)


class Genre(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.ManyToManyField(Author, db_table="book_author")
    summary = models.CharField('Summary', max_length=250)
    imprint = models.CharField('Imprint', max_length=50)
    ISBN = models.CharField('ISBN', max_length=50)
    genre = models.ForeignKey(Genre, related_name="genre", on_delete=models.CASCADE)
    language = models.OneToOneField(Language, blank=True, related_name="language", on_delete=models.CASCADE)

    def __str__(self):
        return 'The Book with title: %s and Author: %s with sumary: %s of the imprint %s with ISBN %s have this genre: %s and this language: %s' % (
        self.title, self.author, self.summary, self.imprint, self.ISBN, self.genre, self.language)


class BoosInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    uniqueId = models.CharField('Id', max_length=50)
    due_back = models.DateTimeField("Due back", default=now, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m',
                              help_text='Disponibility of the book')
    book = models.OneToOneField(Book, blank=True, related_name="book", on_delete=models.CASCADE)

    def __str__(self):
        return 'This BookInstance with %s id, due back to %s with status %s of the book %s' % (self.uniqueId, self.due_back, self.status, self.book)
