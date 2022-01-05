# Generated by Django 3.2.6 on 2021-12-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_content_home_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='content_home',
            name='categories',
        ),
        migrations.DeleteModel(
            name='categories',
        ),
    ]
