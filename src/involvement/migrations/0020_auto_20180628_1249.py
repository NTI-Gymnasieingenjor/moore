# Generated by Django 2.0.5 on 2018-06-28 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('involvement', '0019_role_contact_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactcard',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='contactcard',
            name='description_sv',
        ),
        migrations.RemoveField(
            model_name='contactcard',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactcard',
            name='role_text_en',
        ),
        migrations.RemoveField(
            model_name='contactcard',
            name='role_text_sv',
        ),
        migrations.RemoveField(
            model_name='contactcard',
            name='name',
        ),
    ]
