# Generated by Django 3.0.3 on 2020-03-31 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0005_auto_20200326_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itm',
            name='Itm_image',
            field=models.CharField(default='https://assets.bonappetit.com/photos/5c62e4a3e81bbf522a9579ce/master/pass/milk-bread.jpg', max_length=500),
        ),
    ]
