# Generated by Django 2.1.7 on 2019-08-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_add_index_json_url_to_print'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pushbullet_access_token',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
