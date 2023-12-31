# Generated by Django 4.1.6 on 2023-10-10 23:44

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Объявление')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание')),
                ('category', models.CharField(choices=[('TA', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('TR', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('SM', 'Кузнецы'), ('TN', 'Кожевники'), ('PT', 'Зельевары'), ('SP', 'Мастера заклинаний')], default='TA', max_length=2, verbose_name='Категория')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('preview', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('author', models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
