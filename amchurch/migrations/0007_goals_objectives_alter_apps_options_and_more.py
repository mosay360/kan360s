# Generated by Django 4.0.1 on 2022-04-15 10:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amchurch', '0006_apps_active_wep1_active_weps_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('goImage', models.ImageField(upload_to='pic_goal')),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('objImage', models.ImageField(upload_to='pic_object')),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='apps',
            options={'managed': True, 'verbose_name': 'Apps', 'verbose_name_plural': 'Apps'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'managed': True, 'verbose_name': 'portfolio', 'verbose_name_plural': 'portfolio'},
        ),
        migrations.AlterModelOptions(
            name='wep1',
            options={'managed': True, 'verbose_name': 'Wep1', 'verbose_name_plural': 'Wep1'},
        ),
        migrations.AlterModelOptions(
            name='weps',
            options={'managed': True, 'verbose_name': 'Webs', 'verbose_name_plural': 'Webs'},
        ),
        migrations.AlterField(
            model_name='apps',
            name='Desc',
            field=ckeditor.fields.RichTextField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='wep1',
            name='Desc',
            field=ckeditor.fields.RichTextField(default=b'I01\n', null=True),
        ),
        migrations.AlterField(
            model_name='weps',
            name='Desc',
            field=ckeditor.fields.RichTextField(default=b'I01\n', null=True),
        ),
        migrations.AlterModelTable(
            name='apps',
            table='',
        ),
        migrations.AlterModelTable(
            name='portfolio',
            table='',
        ),
        migrations.AlterModelTable(
            name='wep1',
            table='',
        ),
        migrations.AlterModelTable(
            name='weps',
            table='',
        ),
    ]
