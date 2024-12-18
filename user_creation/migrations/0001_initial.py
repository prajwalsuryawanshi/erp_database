# Generated by Django 5.1.2 on 2024-12-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=35)),
                ('user_type', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
