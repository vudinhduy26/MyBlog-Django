# Generated by Django 3.2.6 on 2021-12-27 11:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_content_home_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='datetimee',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='categorie_child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_child', models.SlugField(unique=True)),
                ('datetime_child', models.DateTimeField(auto_now_add=True)),
                ('categorie_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categorie')),
            ],
        ),
        migrations.AlterField(
            model_name='content_home',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categorie_child'),
        ),
    ]
