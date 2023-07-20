# Generated by Django 4.2.2 on 2023-06-27 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Author')),
                ('bio', models.TextField(blank=True, verbose_name='Biography')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(blank=True, verbose_name='Article')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of publication of the article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.author', verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category', verbose_name='Category')),
                ('tags', models.ManyToManyField(related_name='articles', to='blogapp.tag', verbose_name='')),
            ],
        ),
    ]