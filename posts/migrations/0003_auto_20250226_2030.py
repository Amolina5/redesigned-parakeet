# Generated by Django 5.1.6 on 2025-02-26 20:30

from django.db import migrations


def populate_status(apps, schemaedit):
    entries = {
        "published": "A post that is visible to all",
        "draft": "A post not yet ready for publication",
        "archived": "An older post that is for logged in users"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status_obj = Status (name=key, description=value)
        status_obj.save()
        


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status_post_status'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]
