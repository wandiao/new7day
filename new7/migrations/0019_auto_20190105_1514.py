# Generated by Django 2.1 on 2019-01-05 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0018_auto_20190102_2053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopincome',
            options={'verbose_name': '店面收入', 'verbose_name_plural': '店面收入'},
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='from_depot',
            field=models.ForeignKey(blank=True, help_text='来源仓库', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='from_depot', to='new7.Depot', verbose_name='来源仓库'),
        ),
    ]
