# Generated by Django 2.1.2 on 2019-02-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0004_remove_debate_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]