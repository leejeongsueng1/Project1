# Generated by Django 4.0.3 on 2022-03-08 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_cert',
            field=models.CharField(max_length=12, verbose_name='유저 관리번호'),
        ),
    ]
