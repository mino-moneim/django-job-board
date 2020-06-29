# Generated by Django 3.0.7 on 2020-06-28 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0010_apply_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apply',
            name='cv',
            field=models.FileField(upload_to='apply/'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]