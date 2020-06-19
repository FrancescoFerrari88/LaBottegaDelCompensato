# Generated by Django 3.0.7 on 2020-06-18 10:38

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('mainSite', '0002_event_homesection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]