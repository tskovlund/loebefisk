# Generated by Django 2.1.2 on 2018-10-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
            ],
        ),
    ]
