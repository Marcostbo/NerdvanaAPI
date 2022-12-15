# Generated by Django 4.0.5 on 2022-12-02 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerdvanapp', '0019_pricealert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricealert',
            name='created_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pricealert',
            name='link_resolved',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='pricealert',
            name='price_resolved',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pricealert',
            name='resolved_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
