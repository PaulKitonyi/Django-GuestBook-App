# Generated by Django 2.0.3 on 2018-04-02 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
