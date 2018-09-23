# Generated by Django 2.1 on 2018-09-23 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new7', '0009_merge_20180915_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('count', models.IntegerField(default=1, help_text='数量', verbose_name='数量')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.AddField(
            model_name='depot',
            name='desc',
            field=models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.IntegerField(default=0, help_text='库存', verbose_name='库存'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='goods',
            field=models.ForeignKey(blank=True, help_text='商品', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Goods', verbose_name='商品'),
        ),
    ]
