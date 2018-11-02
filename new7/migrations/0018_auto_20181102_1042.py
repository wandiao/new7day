# Generated by Django 2.1 on 2018-11-02 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0017_auto_20181102_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='in_price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='商品进价', max_digits=10, verbose_name='商品进价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='商品售价', max_digits=10, verbose_name='商品售价'),
        ),
    ]
