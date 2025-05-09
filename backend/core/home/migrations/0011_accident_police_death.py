# Generated by Django 5.1.6 on 2025-05-08 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_patient_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='police',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hosptial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.hospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.accident')),
            ],
        ),
    ]
