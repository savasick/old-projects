from django.db import models
from django.core.validators import FileExtensionValidator

from django.urls import reverse



class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Language(models.Model):
    name = models.CharField(max_length=200,help_text="Enter the book language", default='eng')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, default="Have not name")
    author = models.ManyToManyField(Author, help_text="Select a Author", blank=True)
    bookfile = models.FileField(upload_to ='books/', blank=True, null=True,
                                validators=[FileExtensionValidator(allowed_extensions=["pdf", "epub"])])
    #bookfileEPUB = models.FileField(upload_to ='books/', blank=True, null=True,
    #                            validators=[FileExtensionValidator(allowed_extensions=["epub"])])
    description = models.TextField(max_length=1500, help_text="Enter a description", blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=17, unique=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.title}"






