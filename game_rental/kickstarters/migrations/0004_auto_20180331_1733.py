# Generated by Django 2.0.3 on 2018-03-31 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kickstarters', '0003_kickstarter_sort_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kickstarter',
            name='sort_category',
            field=models.CharField(max_length=20),
        ),
    ]
