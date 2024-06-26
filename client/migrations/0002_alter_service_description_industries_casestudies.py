# Generated by Django 4.2.7 on 2024-03-26 05:22

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('title', models.CharField(max_length=90)),
                ('core_line', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='services/')),
                ('description', froala_editor.fields.FroalaField()),
                ('tags', models.ManyToManyField(to='client.tag')),
            ],
        ),
        migrations.CreateModel(
            name='CaseStudies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('slug', models.SlugField(max_length=300)),
                ('title', models.CharField(max_length=90)),
                ('core_line', models.CharField(max_length=400)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='services/')),
                ('square_image', models.ImageField(upload_to='services/')),
                ('description', froala_editor.fields.FroalaField()),
                ('tags', models.ManyToManyField(to='client.tag')),
            ],
        ),
    ]
