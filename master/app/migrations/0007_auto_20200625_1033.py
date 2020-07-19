# Generated by Django 3.0.7 on 2020-06-25 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20200619_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorrole',
            name='associated_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='questionchoice',
            name='correct_answer',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
