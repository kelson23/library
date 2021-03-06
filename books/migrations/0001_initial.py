# Generated by Django 4.0.5 on 2022-06-06 20:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idCategory', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('idBook', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('bookCover', models.ImageField(upload_to='images/')),
                ('author', models.CharField(max_length=255)),
                ('publishDate', models.DateField(auto_now_add=True)),
                ('pages', models.IntegerField()),
                ('createAt', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
        ),
    ]
