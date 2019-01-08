# Generated by Django 2.1 on 2019-01-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0023_shopinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopinventory',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='商品成本', max_digits=10, verbose_name='商品成本'),
        ),
    ]
