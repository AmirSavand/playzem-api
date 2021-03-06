# Generated by Django 2.1.5 on 2019-01-31 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Party categories',
                'ordering': ('id',),
            },
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ('id',), 'verbose_name_plural': 'Parties'},
        ),
        migrations.AddField(
            model_name='partycategory',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='party_category', to='party.Party'),
        ),
        migrations.AlterUniqueTogether(
            name='partycategory',
            unique_together={('party', 'name')},
        ),
    ]
