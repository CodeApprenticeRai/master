# Generated by Django 3.0.7 on 2020-07-19 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200701_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructorrole',
            old_name='associated_user',
            new_name='associated_instructor',
        ),
        migrations.RemoveField(
            model_name='instructorrole',
            name='associated_course',
        ),
        migrations.AddField(
            model_name='instructorrole',
            name='associated_challenge',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='app.Challenge'),
            preserve_default=False,
        ),
    ]
