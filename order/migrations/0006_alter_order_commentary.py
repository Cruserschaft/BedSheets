# Generated by Django 4.1.2 on 2022-10-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='commentary',
            field=models.TextField(blank=True, verbose_name='Коментарій'),
        ),
    ]