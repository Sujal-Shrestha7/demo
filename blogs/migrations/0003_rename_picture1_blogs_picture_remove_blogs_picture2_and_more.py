# Generated by Django 4.1.7 on 2023-03-03 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogs_picture1_alter_blogs_picture2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='picture1',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='picture2',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='picture3',
        ),
    ]