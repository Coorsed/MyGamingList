# Generated by Django 5.0.6 on 2024-07-07 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_alter_project_options_project_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
    ]
