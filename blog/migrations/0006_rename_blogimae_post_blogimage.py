# Generated by Django 4.0.1 on 2022-02-11 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_blogimae'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blogImae',
            new_name='blogImage',
        ),
    ]
