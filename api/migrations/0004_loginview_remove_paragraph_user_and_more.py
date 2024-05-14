# Generated by Django 4.2.5 on 2024-05-14 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rest_framework.views


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_customuser_dob_remove_customuser_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginView',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(rest_framework.views.APIView, 'api.customuser'),
        ),
        migrations.RemoveField(
            model_name='paragraph',
            name='user',
        ),
        migrations.AddField(
            model_name='paragraph',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]