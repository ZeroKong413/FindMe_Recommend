# Generated by Django 5.0.7 on 2024-07-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A_Book_Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='books/A')),
            ],
        ),
        migrations.CreateModel(
            name='A_Movie_Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('actors', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='posters/A')),
            ],
        ),
        migrations.CreateModel(
            name='A_Song_Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('singer', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='songs/A')),
            ],
        ),
        migrations.CreateModel(
            name='B_Book_Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='books/B')),
            ],
        ),
        migrations.CreateModel(
            name='B_Movie_Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('actors', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='posters/B')),
            ],
        ),
        migrations.CreateModel(
            name='B_Song_Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('singer', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='songs/B')),
            ],
        ),
        migrations.CreateModel(
            name='C_Book_Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='books/C')),
            ],
        ),
        migrations.CreateModel(
            name='C_Movie_Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('actors', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='posters/C')),
            ],
        ),
        migrations.CreateModel(
            name='C_Song_Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('singer', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='songs/C')),
            ],
        ),
    ]
