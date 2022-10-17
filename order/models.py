from django.db import models


class PostType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва")
    order = models.SmallIntegerField(unique=True, verbose_name="Порядок")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Доставка"
        ordering = ('order',)


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Ім'я")
    phone = models.CharField(max_length=13, verbose_name="Ім'я")
    email = models.CharField(max_length=50, verbose_name="Email")
    city = models.CharField(max_length=50, verbose_name="Ім'я")
    address = models.CharField(max_length=50, verbose_name="Ім'я")
    post = models.ForeignKey(PostType, on_delete=models.PROTECT, verbose_name="Доставка", related_name="+")
    post_code = models.CharField(max_length=5)
    commentary = models.TextField(verbose_name="Коментарій")
    order = models.TextField(verbose_name="Замовлення", default="", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата і час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата і час оновлення")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = verbose_name_plural = "Замовлення"
        ordering = ("time_update", "time_create")
