# Generated by Django 3.0.7 on 2020-08-02 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200801_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengereportquestionsubmission',
            name='parent_challenge_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ChallengeReport'),
        ),
    ]
