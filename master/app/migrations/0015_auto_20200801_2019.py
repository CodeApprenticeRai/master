# Generated by Django 3.0.7 on 2020-08-02 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_auto_20200730_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_submitted', models.DateTimeField(auto_now=True)),
                ('questions_count', models.IntegerField()),
                ('correct_answer_coutn', models.IntegerField()),
                ('associated_candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('associated_challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeReportQuestionSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associated_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
                ('parent_challenge_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Challenge')),
                ('submitted_question_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.QuestionChoice')),
            ],
        ),
        migrations.DeleteModel(
            name='Scorecard',
        ),
    ]