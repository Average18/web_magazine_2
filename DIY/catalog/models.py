from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Каталог',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Tag(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    author = models.ForeignKey(
        User,
        related_name='blog_posts',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True
    )
    #image = models.ImageField(
       # upload_to='articles/',
       # verbose_name='Изображение'
    #)
    tags = models.ManyToManyField(
        Tag,
        related_name='post',
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название товара'
    )
   # image = models.ImageField(
   #     upload_to='articles/',
    #    verbose_name='Изображение'
    #)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )#
    body = models.TextField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'product'

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=150)
    body = models.TextField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        related_name='comment',
        on_delete=models.CASCADE
    )