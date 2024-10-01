# Generated by Django 3.2.23 on 2024-04-23 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acd_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='emotion_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acd_app.student_table')),
            ],
        ),
    ]