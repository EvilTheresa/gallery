# Generated by Django 5.1 on 2024-08-31 12:56
import uuid

from django.db import migrations, models

def gen_uuid(apps, schema_editor):
    Photo = apps.get_model("webapp", "Photo")
    for row in Photo.objects.all():
        row.access_token = uuid.uuid4()
        row.save(update_fields=["access_token"])

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_photo_access_token_alter_photo_author'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
