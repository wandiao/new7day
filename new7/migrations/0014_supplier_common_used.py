# Generated by Django 2.1 on 2018-12-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0013_auto_20181209_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='common_used',
            field=models.BooleanField(blank=True, default=True, help_text='是否可以被普通员工所用', null=True),
        ),
    ]
