# Generated by Django 4.1.2 on 2022-10-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.TextField(blank=True, default='', verbose_name='Замовлення'),
        ),
    ]