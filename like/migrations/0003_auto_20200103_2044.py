# Generated by Django 3.0 on 2020-01-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0002_auto_20191229_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='kind',
            field=models.IntegerField(choices=[(1, 'User'), (2, 'Party'), (3, 'Category'), (4, 'Song')], db_index=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
