# Generated by Django 3.1.3 on 2020-12-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamtechs', '0004_auto_20201226_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects_webstartup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='projects-done')),
            ],
            options={
                'verbose_name_plural': 'Projects_loan',
            },
        ),
    ]
