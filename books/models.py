from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to="book_storage/%Y/%m/%d")
    photo = models.ImageField(upload_to="image/%Y/%m/%d", blank=True)
    file = models.FileField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='book')
    owner = models.ForeignKey(User, models.CASCADE,related_name='books')

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*arg, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parrent = models.ForeignKey('self',null=True,related_name='replies',on_delete=models.CASCADE,blank=True)

    @property
    def is_parrent(self):
        if self.parrent is not None:
            return False
        return True

class Rate(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rate')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='rates')
    timestamp = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(null=True)