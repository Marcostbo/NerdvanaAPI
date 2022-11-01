# Generated by Django 4.0.5 on 2022-10-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_validateemailcode_passwordrecoverycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordrecoverycode',
            name='reason',
            field=models.CharField(choices=[('Password Recovery', 'Password Recovery'), ('Email Validation', 'Email Validation')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='validateemailcode',
            name='reason',
            field=models.CharField(choices=[('Password Recovery', 'Password Recovery'), ('Email Validation', 'Email Validation')], max_length=20, null=True),
        ),
    ]