# Generated by Django 3.0.7 on 2020-08-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200801_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengereport',
            name='correct_answer_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='challengereport',
            name='questions_count',
            field=models.IntegerField(null=True),
        ),
    ]