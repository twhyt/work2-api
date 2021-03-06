# Generated by Django 3.2.4 on 2021-07-02 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/category')),
                ('detail', models.TextField(max_length=255)),
                ('is_enable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('detail', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/product')),
                ('is_enable', models.BooleanField(default=True)),
                ('created_datetime', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='myapi.product')),
            ],
            options={
                'verbose_name': 'img',
                'verbose_name_plural': 'img',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
