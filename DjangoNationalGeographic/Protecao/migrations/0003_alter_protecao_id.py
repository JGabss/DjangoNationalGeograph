# Generated by Django 3.2.8 on 2021-10-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Protecao', '0002_auto_20211015_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protecao',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
