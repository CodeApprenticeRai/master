# Generated by Django 3.0.7 on 2020-08-02 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200801_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challengereport',
            old_name='correct_answer_coutn',
            new_name='correct_answer_count',
        ),
    ]