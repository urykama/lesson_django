from django.db import models


# Create your models here.
# здесь будут храниться модели
class Category(models.Model):
    # Id не надо
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    # # основные типы полей
    # # дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # # числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # логический
    # models.BooleanField
    # # Байты
    # models.BinaryField
    # # картинка
    # models.ImageField
    # # файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # связь с категорией
    # один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # связь с тэгом
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
