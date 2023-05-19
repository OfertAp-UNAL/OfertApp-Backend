# Generated by Django 3.2.16 on 2023-05-19 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsupport',
            name='user',
            field=models.ForeignKey(db_column='usrId', on_delete=django.db.models.deletion.CASCADE, related_name='reportsSupport', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='publication',
            field=models.ForeignKey(db_column='pubId', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='publications.publication'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(db_column='usrId', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
    ]
