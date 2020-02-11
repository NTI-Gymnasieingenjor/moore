# Generated by Django 2.2.9 on 2020-02-07 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('home', '0025_banner_featured_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='featured_media',
        ),
        migrations.AddField(
            model_name='banner',
            name='video',
            field=models.ForeignKey(blank=True, help_text='Banner video media. If video is not supported by the browser, the image is shown instead.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
    ]
