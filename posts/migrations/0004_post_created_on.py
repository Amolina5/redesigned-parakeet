# Generated by Django 5.1.6 on 2025-03-01 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20250226_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),  # Use datetime.datetime.now
            preserve_default=False,
        ),
    ]

