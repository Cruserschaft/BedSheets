# Generated by Django 4.1.2 on 2022-10-12 17:55

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Тег')),
                ('cost', models.IntegerField(verbose_name='Вартість')),
                ('about', models.TextField(blank=True, verbose_name='Опис')),
                ('sales', models.IntegerField(default=0, verbose_name='Продажі')),
                ('image', models.ImageField(upload_to=product.models.Product.get_file_name, verbose_name='Зображення')),
                ('access', models.BooleanField(default=True, verbose_name='Доступ')),
                ('favorite', models.BooleanField(default=False, verbose_name='Обране (на головну)')),
                ('datetime_create', models.DateTimeField(auto_now=True, verbose_name='Дата і час створення/оновлення')),
            ],
            options={
                'verbose_name': 'Товари',
                'verbose_name_plural': 'Товари',
                'ordering': ('datetime_create',),
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Тег')),
                ('order', models.PositiveSmallIntegerField(unique=True, verbose_name='Порядок')),
                ('access', models.BooleanField(default=True, verbose_name='Доступ')),
            ],
            options={
                'verbose_name': 'Тип Товару',
                'verbose_name_plural': 'Тип Товару',
                'ordering': ('access', 'order'),
            },
        ),
        migrations.CreateModel(
            name='ProductSubtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('cost', models.IntegerField(verbose_name='Вартість')),
                ('access', models.BooleanField(default=True, verbose_name='Доступ')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.producttype', verbose_name='Тип'),
        ),
    ]
