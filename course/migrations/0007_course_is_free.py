# Generated by Django 4.1.7 on 2023-03-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
    ]
