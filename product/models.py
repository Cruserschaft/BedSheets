import os
import uuid
from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва")
    title_extra = models.CharField(max_length=100, blank=True, verbose_name="Підтип", null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="Тег")
    order = models.PositiveSmallIntegerField(unique=True, verbose_name="Порядок")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        if self.title_extra:
            return f"{self.title}: {self.title_extra}"
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = "Тип Товару"
        ordering = ("access", "order")


class Product(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/products/', filename)

    title = models.CharField(max_length=100, db_index=True, verbose_name="Назва")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="Тег")
    product_type = models.ManyToManyField(ProductType, verbose_name="Тип товару")
    cost = models.IntegerField(verbose_name="Вартість")
    about = models.TextField(blank=True, verbose_name="Опис")
    sales = models.IntegerField(default=0, verbose_name="Продажі")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    access = models.BooleanField(default=True, verbose_name="Доступ")
    favorite = models.BooleanField(default=False, verbose_name="Обране (на головну)")
    datetime_create = models.DateTimeField(auto_now=True, verbose_name="Дата і час створення/оновлення")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = "Товари"
        ordering = ("datetime_create", )

