# Generated by Django 2.2.1 on 2019-12-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191206_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Del',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.ManyToManyField(to='posts.Like')),
            ],
        ),
    ]
