# Generated by Django 2.1 on 2019-01-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0017_auto_20181229_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsdamaged',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='价格', max_digits=10, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goodsrecord',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='价格', max_digits=10, verbose_name='价格'),
        ),
    ]
