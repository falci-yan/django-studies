# Generated by Django 5.1.5 on 2025-03-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
