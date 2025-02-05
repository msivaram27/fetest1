# Generated by Django 5.0.7 on 2024-10-11 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('srrp', '0003_recipe_rating_count_alter_recipe_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='srrp.recipe')),
            ],
        ),
    ]
