# Generated by Django 4.2.7 on 2024-03-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_casestudies_name_alter_industries_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudies',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='casestudies',
            name='title',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='industries',
            name='title',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=180),
        ),
    ]
