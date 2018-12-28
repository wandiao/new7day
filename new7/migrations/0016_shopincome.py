# Generated by Django 2.1 on 2018-12-28 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0015_auto_20181209_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('income', models.DecimalField(decimal_places=2, default=0, help_text='收入', max_digits=10, verbose_name='收入')),
                ('shop', models.ForeignKey(help_text='店面', on_delete=django.db.models.deletion.PROTECT, to='new7.Shop', verbose_name='店面')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]