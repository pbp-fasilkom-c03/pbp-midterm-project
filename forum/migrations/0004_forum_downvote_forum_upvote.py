# Generated by Django 4.1 on 2022-10-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_forum_created_at_forum_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='forum',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
